import random
from typing import Dict, Any
from langchain_core.tools import tool

@tool
def create_calendar_event(title: str, start_time: str, end_time: str, description: str = "") -> Dict[str, Any]:
    """
    Create a calendar event.
    Returns the created event details.
    """
    print(f"Creating calendar event: {title} from {start_time} to {end_time}")
    
    return {
        "status": "success",
        "event_id": f"EVT{random.randint(1000, 9999)}",
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "description": description,
        "message": "Event added to calendar successfully."
    }
