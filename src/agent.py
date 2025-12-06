import os
import datetime
from typing import Literal

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from src.state import AgentState
from src.tools import (
    search_flights, book_flight,
    search_hotels, book_hotel,
    get_weather, search_attractions,
    create_calendar_event, search_restaurants,
    get_visa_info, search_trains, search_events
)
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define tools
tools = [
    search_flights, book_flight,
    search_hotels, book_hotel,
    get_weather, search_attractions,
    create_calendar_event, search_restaurants,
    get_visa_info, search_trains, search_events
]

# Bind tools to LLM
llm_with_tools = llm.bind_tools(tools)

# Define the reasoner node
def reasoner(state: AgentState, config: RunnableConfig):
    """
    The reasoner node decides what to do next: call a tool or end the conversation.
    """
    messages = state["messages"]
    
    # System prompt to guide the agent
    system_prompt = (
        f"You are an expert travel agent and API orchestrator. Current date: {datetime.date.today()}. "
        "Your goal is to help users plan trips by coordinating flights, hotels, trains, weather, attractions, restaurants, events, and visa requirements. "
        "Always check the weather before suggesting outdoor activities. "
        "IMPORTANT: If you cannot find exact flights or hotels for specific dates, DO NOT FAIL. "
        "Instead, provide REALISTIC ESTIMATES based on the search results (e.g., 'Typical flights cost around $X'). "
        "Assume availability for the purpose of this plan. "
        "Assume availability for the purpose of this plan. "
        "If you need to book something, ask for confirmation first if the user hasn't explicitly said so. "
        "CLARIFICATION: You cannot perform real bookings. When asked to book, generate a simulated booking confirmation. "
        "Always respond in the same language as the user's input. "
        "Be helpful, concise, and professional."
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
    ])
    
    chain = prompt | llm_with_tools
    response = chain.invoke({"messages": messages})
    
    return {"messages": [response]}

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("reasoner", reasoner)
workflow.add_node("tools", ToolNode(tools))

# Define edges
workflow.set_entry_point("reasoner")

def should_continue(state: AgentState) -> Literal["tools", END]:
    """
    Determine whether to continue to tools or end.
    """
    last_message = state["messages"][-1]
    
    if last_message.tool_calls:
        return "tools"
    return END

workflow.add_conditional_edges(
    "reasoner",
    should_continue,
)

workflow.add_edge("tools", "reasoner")

# Compile the graph
app = workflow.compile()
