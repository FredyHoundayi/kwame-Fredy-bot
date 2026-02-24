
import requests
from langchain_core.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()


@tool
def get_weather(query: str) -> str:
    """Search weatherapi to get the current weather"""
    endpoint = f"http://api.weatherapi.com/v1/current.json?key={os.getenv("GETWEATHER_API_KEY")}&q={query}"
    response = requests.get(endpoint)
    data = response.json()

    if data.get("location"):
        return str(data)
    else:
        return "Weather Data Not Found"

#print(get_weather.invoke("london"))