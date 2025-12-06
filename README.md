# ✈️ Autonomous API Orchestration Agent

An intelligent agent capable of orchestrating multiple APIs to accomplish complex tasks, built for the AI Demos Hackathon.

## 🌟 Features

- **Multi-Step Reasoning**: Uses LangGraph to plan and execute complex travel itineraries.
- **Tool Orchestration**: seamlessly integrates Flight, Hotel, Weather, and Attraction search tools.
- **Streamlit Frontend**: A user-friendly chat interface to interact with the agent.
- **CLI Support**: A command-line interface for quick testing.
- **Mock APIs**: Realistic mock data for robust demonstration without API costs.

## 🛠️ Tech Stack

- **Framework**: LangChain, LangGraph
- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Frontend**: Streamlit
- **Language**: Python 3.10+

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd API-Orchestration-Agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your `GOOGLE_API_KEY` to `.env`

### Usage

#### Run the Streamlit App (Recommended)
```bash
streamlit run app.py
```

#### Run the CLI
```bash
python main.py
```

## 🧩 Architecture

The agent uses a **ReAct-style** architecture implemented with **LangGraph**:

1. **Reasoner Node**: Analyzes the user request and conversation history to decide the next action.
2. **Tool Node**: Executes the selected tools (Flights, Hotels, etc.) and returns the output.
3. **Loop**: The graph cycles between Reasoner and Tool nodes until the task is completed.

## 📝 Example Queries

- "Plan a 3-day trip to Paris from New York starting next Friday. I need a flight, a hotel in the city center, and a list of top museums to visit."
- "Find me a flight from London to Tokyo on Dec 25th and check the weather there."
