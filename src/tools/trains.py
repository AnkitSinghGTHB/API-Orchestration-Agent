from typing import Dict, Any
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_trains(origin: str, destination: str, date: str) -> str:
    """
    Search for trains between two cities.
    Returns a summary of available trains, schedules, and estimated prices.
    """
    query = f"trains from {origin} to {destination} on {date} schedule and ticket price"
    print(f"Searching web for: {query}")
    return perform_search(query)
