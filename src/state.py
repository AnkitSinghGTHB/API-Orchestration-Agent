import operator
from typing import Annotated, List, TypedDict, Union, Dict, Any
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[List[BaseMessage], operator.add]
    plan: List[str]
    user_preferences: Dict[str, Any]
    results: Dict[str, Any]
