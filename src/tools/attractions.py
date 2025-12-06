from typing import List, Dict, Any, Union
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_attractions(location: str) -> str:
    """
    Search for top tourist attractions in a specific location using web search.
    Returns a summary of attractions found on the web.
    """
    query = f"top tourist attractions in {location}"
    print(f"Searching web for: {query}")
    return perform_search(query)
