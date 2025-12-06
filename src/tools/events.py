from typing import Dict, Any
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_events(location: str, date_range: str, event_type: str = "cultural") -> str:
    """
    Search for festivals and events in a location during a specific date range.
    Returns a summary of events found.
    """
    query = f"{event_type} festivals and events in {location} during {date_range}"
    print(f"Searching web for: {query}")
    return perform_search(query)
