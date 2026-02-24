import serpapi
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.tools import tool
import trafilatura
api_key = os.getenv("SERP_API_KEY")

@tool
def search_google(query: str) -> str:
    """Search Google in real time for up-to-date information, news, facts, or recent events.

    Use this tool when:
    - the question requires current or live information
    - you need recent news or updates
    - the answer is not likely in the model's training data
    - searching the web is necessary

    Input:
        query: search keywords or question

    Output:
        A summarized list of relevant search results with titles, snippets, and links. joined as string
    """
    
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": 5
    }
    
    try:
        search = serpapi.search(params)
        results = search.as_dict()
    
        essential = []

        for r in results.get("organic_results", []):
            title = r.get("title", "")
            snippet = r.get("snippet", "")
            link = r.get("link", "")
            
            essential.append(
                f"{title}\n{snippet}\n{link}"
            )

        return "\n\n".join(essential)
    
    except Exception as e:
        return f"Error during Google search: {str(e)}"
print(search_google.invoke("What is the weather in New York?"))