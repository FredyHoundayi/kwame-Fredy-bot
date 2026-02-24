from tavily import TavilyClient
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
from langchain_core.tools import tool
load_dotenv()


@tool
def tav_search(query: str) -> str:
    """
    Perform a real-time web search using Tavily and return concise, relevant, and summarized results.

    Use this tool when:
    - you need up-to-date or live information
    - the question involves recent events, news, or trends
    - factual verification is required
    - external knowledge beyond the model’s training data is needed

    Input:
        query: a question or search keywords

    Output:
        A summarized list of relevant results with titles, extracted content, and source URLs.
    """
    tavily_search = TavilySearch(
        api_key=os.getenv("TAVILY_API_KEY"), 
        max_results=2, 
        search_depth='advanced'
    )

    results = tavily_search.invoke(query)

    
    return str(results)
#print(tav_search.invoke("Quelle est la date daujourd hui"))*

