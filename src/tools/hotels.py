from typing import List, Dict, Any, Union
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_hotels(location: str, check_in_date: str, check_out_date: str) -> str:
    """
    Search for hotels in a specific location for a given date range using web search.
    Returns a summary of available hotels found on the web.
    """
    query = f"hotel prices in {location} check-in {check_in_date} check-out {check_out_date}"
    print(f"Searching web for: {query}")
    return perform_search(query)

@tool
def book_hotel(hotel_id: str) -> Dict[str, Any]:
    """
    Book a hotel using its hotel_id.
    Returns a booking confirmation.
    """
    print(f"Booking hotel {hotel_id}")
    
    return {
        "status": "confirmed",
        "hotel_id": hotel_id,
        "booking_reference": f"HTBR-REAL-{hotel_id[-4:]}",
        "message": f"Hotel {hotel_id} successfully booked (simulated)."
    }
