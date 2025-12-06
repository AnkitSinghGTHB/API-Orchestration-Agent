from typing import List, Dict, Any, Union
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_restaurants(location: str, cuisine: str = None) -> str:
    """
    Search for restaurants in a specific location using web search.
    Returns a summary of restaurants found on the web.
    """
    query = f"specific restaurant names with ratings and menu prices for {cuisine if cuisine else ''} food in {location}"
    print(f"Searching web for: {query}")
    return perform_search(query)
