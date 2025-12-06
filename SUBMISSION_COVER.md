# AI Travel Orchestrator - Hackathon Submission Cover

## 1. LangChain/LangGraph Setup
The core of the **AI Travel Orchestrator** is built on **LangGraph**, utilizing a cyclic state graph to manage the agent's reasoning loop.

*   **State Management**: We use a typed `AgentState` that persists the conversation history (`messages`) across multiple turns.
*   **Graph Architecture**:
    *   **Reasoner Node**: Powered by **Google Gemini 2.5**, this node analyzes the user's request and current state to decide the next best action (calling a tool or providing a final answer).
    *   **Tool Node**: A prebuilt LangGraph node that executes the Python functions selected by the LLM.
    *   **Conditional Edges**: The graph dynamically decides whether to loop back to the *Reasoner* (if more information is needed) or terminate (if the task is complete), enabling complex, multi-step workflows.

## 2. Key Components & Tools
*   **LLM**: Google Gemini 2.5 (Flash/Pro) via `langchain-google-genai` for high-speed reasoning and natural language generation.
*   **Orchestration**: `LangGraph` for stateful, cyclic agentic workflows.
*   **Frontend**: `Streamlit` for a clean, interactive chat interface with custom styling.
*   **Real-Time Data Tools**: A suite of 9 custom tools powered by **DuckDuckGo Search (`ddgs`)** to fetch live data without expensive API subscriptions:
    *   ✈️ `search_flights` / `book_flight` (Simulated)
    *   🏨 `search_hotels` / `book_hotel` (Simulated)
    *   🚆 `search_trains` (Real-time schedules)
    *   🛂 `get_visa_info` (Official requirements)
    *   🎉 `search_events` (Local festivals & events)
    *   🍽️ `search_restaurants` (Specific names & ratings)
    *   ☀️ `get_weather`
    *   🎡 `search_attractions`
    *   🗓️ `create_calendar_event`

## 3. Interaction & Reasoning
The agent operates using a **ReAct (Reasoning + Acting)** paradigm:
1.  **Input Analysis**: It parses complex, natural language queries (e.g., "Plan a 2-week trip to India starting Jan 1st with a 25k budget").
2.  **Dynamic Planning**: It breaks the goal down into logical steps—checking visa requirements first, then finding transport, then accommodation, and finally activities.
3.  **Context Awareness**: It injects the **current date** into its context to ensure all plans are temporally accurate.
4.  **Robustness**: If exact booking data is unavailable via search, the agent is instructed to provide **realistic estimates** rather than failing, ensuring a smooth user experience.
5.  **Multi-Language Support**: It automatically detects and responds in the user's preferred language.

## 4. Real-World Problem Solved
**The Problem**: Travel planning is currently a fragmented, high-friction experience. Travelers must juggle multiple tabs—flight search engines, hotel booking sites, government visa portals, weather apps, and travel blogs—to plan a single trip. This context switching is exhausting and often leads to disjointed itineraries.

**The Solution**: The **AI Travel Orchestrator** unifies these disparate sources into a **single, conversational interface**. By orchestrating real-time data from across the web, it allows users to plan entire complex itineraries—from visa checks to dinner reservations—in seconds, acting as a knowledgeable, 24/7 personal travel assistant.
