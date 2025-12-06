from typing import List, Dict, Any, Union
from langchain_core.tools import tool
from src.tools.web_search import perform_search

@tool
def search_flights(origin: str, destination: str, date: str) -> str:
    """
    Search for flights between an origin and a destination on a specific date using web search.
    Returns a summary of available flights found on the web.
    """
    query = f"flight prices from {origin} to {destination} on {date}"
    print(f"Searching web for: {query}")
    return perform_search(query)

@tool
def book_flight(flight_id: str) -> Dict[str, Any]:
    """
    Book a flight using its flight_id.
    Returns a booking confirmation.
    """
    print(f"Booking flight {flight_id}")
    
    return {
        "status": "confirmed",
        "flight_id": flight_id,
        "booking_reference": f"BR-REAL-{flight_id[-4:]}",
        "message": f"Flight {flight_id} successfully booked (simulated)."
    }
