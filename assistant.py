from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from langgraph.prebuilt import create_react_agent

import os


load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
#print("GROQ_API_KEY:", GROQ_API_KEY)
#Set LLM
model=["llama-3.3-70b-versatile","openai/gpt-oss-20b"]

groq_chat=ChatGroq(api_key=GROQ_API_KEY,model=model[0],temperature=0,disable_streaming=False)
#response=groq_chat.invoke([{"role":"user","content":"Write a poem about the sea."}])
#print("Response:", response.content)
#Set Prompt Template
template=ChatPromptTemplate.from_messages([("system","You are Kwame Fredy Bot, my personal assistant. Be helpful and interactive."),("user"," {user_input}")])
parser=StrOutputParser()


llm_chain=template|groq_chat|parser

#response_with_prompt=llm_chain.invoke({"user_input":"What's the weather like today in New York?"},streaming=True)
#print("Response with Prompt Template:", response_with_prompt.content)
"""for chunk in llm_chain.stream({"user_input":"Who is Fredy HOUNDAYI?"}):
    print(chunk, end="", flush=True)"""



"""#Memory
memory=InMemoryChatMessageHistory()
llm_chain_with_memory=template|groq_chat|parser|memory"""



#response_with_memory=llm_chain_with_memory.invoke({"user_input":"Who is Fredy HOUNDAYI?"})

#Tools
from langchain_core.tools import tool
#from tools.google_search_tool import search_google
from tools.tavily_tool import tav_search
from tools.get_weather_tool import get_weather
from tools.article_retriever import online_article_retriever
from tools.files_reader import read_pdf



tools=[get_weather,tav_search,online_article_retriever,read_pdf]


from langgraph.prebuilt import create_react_agent

# system prompt is used to inform the tools available to when to use each
system_prompt = """Act as a helpful assistant.
    Use the tools at your disposal to perform tasks as needed.
        -get_weather: search real time weather related information  based on location ,like time ,date....
        
        -tav_search: Use tavily search when search_google can't provide correct answers or info
    Use the tools only if you don't know the answer.
    Comme resultat final sois concis  et source tes sources au besoins
        -online_article_retriever: Retrieve and parse the content of an online article given its URL .Whe the user input add a url in his question use this tool to extract the content of the article and use it to answer the question
        -read_pdf: Read the content of a PDF file and return it as a string. When the user input add a pdf file in his question use this tool to extract the content of the pdf file and use it to answer the question
    """

# we can initialize the agent using the  model, tools, and system prompt.
agent = create_react_agent(model=groq_chat, tools=tools, prompt=system_prompt)
 



# Test de conversation

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "What are the update in the world")]}

#print_stream(agent.stream(inputs, stream_mode="values"))
print(agent.invoke(inputs))