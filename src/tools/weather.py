from typing import Dict, Any, Union
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def get_weather(location: str, date: str) -> str:
    """
    Get the weather forecast for a specific location and date using web search.
    Returns a summary of the weather forecast found on the web.
    """
    query = f"weather in {location} on {date}"
    print(f"Searching web for: {query}")
    return perform_search(query)
