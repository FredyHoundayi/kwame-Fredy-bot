# app.py
import os
import logging
from dotenv import load_dotenv
import chainlit as cl
from tools import google_search_tool

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# LangChain / Groq imports
try:
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.tools import tool
    from langchain.agents import AgentExecutor, create_tool_calling_agent
    
    # Import des outils (sans Tavily)
    from tools.get_weather_tool import get_weather
    from tools.google_search_tool import search_google
    from tools.article_retriever import online_article_retriever
    from tools.files_reader import read_pdf
    
    logger.info("Toutes les dépendances sont correctement importées")
except ImportError as e:
    logger.error(f"Erreur d'importation : {e}")
    raise

# ⚡ Load environment
try:
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GETWEATHER_API_KEY = os.getenv("GETWEATHER_API_KEY")
    SERP_API_KEY = os.getenv("SERP_API_KEY")
    
    if not all([GROQ_API_KEY, GETWEATHER_API_KEY, SERP_API_KEY]):
        raise ValueError("Une ou plusieurs clés API manquantes dans le fichier .env")
        
    logger.info("Variables d'environnement chargées avec succès")
    
except Exception as e:
    logger.error(f"Erreur lors du chargement des variables d'environnement : {e}")
    raise

# ⚡ Initialize Groq LLM
try:
    groq_chat = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        disable_streaming=True
    )
    logger.info("Modèle Groq initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation du modèle Groq : {e}")
    raise

# ⚡ Initialize prompt template
try:
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful interactive personal assistant."),
        ("user", " {user_input}")
    ])
    parser = StrOutputParser()
    llm_chain = template | groq_chat | parser
    logger.info("Modèle de prompt initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation du modèle de prompt : {e}")
    raise

# ⚡ Tools (sans Tavily)
try:
    tools = [get_weather, search_google, online_article_retriever, read_pdf]
    logger.info("Outils chargés avec succès")
except Exception as e:
    logger.error(f"Erreur lors du chargement des outils : {e}")
    raise

# ⚡ System prompt (sans Tavily)
system_prompt = """Act Kwame Fredy Bot,a helpful personnal assistant of Fredy
    Use the tools at your disposal to perform tasks as needed.
        -get_weather: search real time weather related information  based on location ,like time ,date....
        -search_google: Use google search when you need real-time information
        -online_article_retriever: Retrieve and parse the content of an online article given its URL .Whe the user input add a url in his question use this tool to extract the content of the article and use it to answer the question
        -read_pdf: Read the content of a PDF file and return it as a string. When the user input add a pdf file in his question use this tool to extract the content of the pdf file and use it to answer the question
        -    Use the tools only if you don't know the answer.
          Comme resultat final sois concis  et source tes sources au besoins
    
    """

# ⚡ Initialize agent using LangChain
try:
    agent = create_tool_calling_agent(
        llm=groq_chat,
        tools=tools,
        prompt=ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("placeholder", "{messages}"),
        ])
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    logger.info("Agent LangChain initialisé avec succès")
except Exception as e:
    logger.error(f"Erreur lors de l'initialisation de l'agent LangChain : {e}")
    raise

# ⚡ Chainlit conversation
@cl.on_message
async def main(message: cl.Message):
    try:
        logger.info(f"Nouveau message : {message.content}")
        
        # Vérifier si des fichiers sont uploadés
        uploaded_files = []
        pdf_context = ""
        
        if message.elements:
            for element in message.elements:
                if isinstance(element, cl.File):
                    uploaded_files.append(element)
                    file_path = element.path
                    if file_path.endswith('.pdf'):
                        # Lire le PDF et l'ajouter au contexte
                        from tools.files_reader import read_pdf
                        pdf_content = read_pdf.invoke(file_path)
                        pdf_context += f"\n\n--- Contenu du document '{element.name}' ---\n{pdf_content}\n--- Fin du document ---"

        msg = cl.Message(content="")
        await msg.send()

        # Construire le contexte avec le PDF si présent
        context = message.content
        if pdf_context:
            context = f"Document PDF fourni : {pdf_context}\n\nQuestion de l'utilisateur : {message.content}"
        elif uploaded_files:
            # Autres types de fichiers
            file_info = "\n\nFichiers uploadés:\n"
            for file in uploaded_files:
                file_info += f"- {file.name} (chemin: {file.path})\n"
            context += file_info

        result = await agent_executor.ainvoke({"messages": [("human", context)]})

        # ✅ EXTRACTION PROPRE ET GARANTIE
        if isinstance(result, dict) and "output" in result:
            final_output = result["output"]
        else:
            final_output = str(result)

        # ✅ Affichage clean
        msg.content = final_output
        await msg.update()

    except Exception as e:
        logger.exception("Erreur agent")
        await cl.Message(
            content=f"Désolé, une erreur est survenue : {str(e)}"
        ).send()
