from typing import Dict, Any
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def get_visa_info(country_code: str, origin_country: str) -> str:
    """
    Get visa requirements for a specific country based on the traveler's origin.
    Returns a summary of visa policies, costs, and application details.
    """
    query = f"official visa requirements documents and cost for {origin_country} citizens visiting {country_code} tourist visa"
    print(f"Searching web for: {query}")
    return perform_search(query)
