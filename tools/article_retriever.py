from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os
from langchain_core.tools import tool
import requests
import trafilatura
from langchain_core.tools import tool
load_dotenv()


@tool
def  online_article_retriever(url: str) -> str:
    """
    Retrieve and parse the content of an online article given its URL.

    Use this tool when:
    - you need to extract information from a specific online article
    - the url requires detailed content from a known source
    - you want to analyze or summarize the content of a web page

    Input:
        url: the URL of the online article

    Output:
        The parsed content of the online article as a string."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        content = trafilatura.extract(response.text)
        
        return content[:9000] if content else "No content could be extracted from the provided URL."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching the article: {e}"

#print(online_article_retriever.invoke("https://www.dailydoseofds.com/model-context-protocol-crash-course-part-1/"))