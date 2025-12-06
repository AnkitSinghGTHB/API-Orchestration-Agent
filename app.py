import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from src.agent import app as agent_app
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Travel Orchestrator", page_icon="🌍", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .stChatInput {
        position: fixed;
        bottom: 3rem;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #555;
        text-align: center;
        padding: 10px;
        font-size: 0.8rem;
        border-top: 1px solid #ddd;
        z-index: 100;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🌍 AI Travel Orchestrator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your autonomous agent for planning flights, hotels, trains, and adventures.</div>', unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Google API Key", type="password", value=os.getenv("GOOGLE_API_KEY"))
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    
    st.divider()
    
    st.header("🛠️ Capabilities")
    st.markdown("""
    - **🔍 Search & Plan**: Flights, Hotels, Trains
    - **🛂 Travel Info**: Visa Requirements, Weather
    - **🎡 Explore**: Attractions, Events, Restaurants
    - **📅 Organize**: Calendar Management
    """)
    
    st.divider()
    st.info("ℹ️ **About**: This agent uses **LangGraph** and **Gemini 2.5** to orchestrate real-time travel data.")
    
    st.info("⚠️ Note: All bookings are simulated. Prices are estimates based on web search.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_message_text(message):
    if isinstance(message.content, list):
        # Join all text parts
        return "".join([part.get("text", "") for part in message.content if isinstance(part, dict)])
    return message.content

# Display chat messages
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(get_message_text(message))
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(get_message_text(message))

# Chat input
if prompt := st.chat_input("Plan a trip to Paris..."):
    if not prompt.strip():
        st.warning("Please enter a valid request.")
        st.stop()
    # Add user message to history
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run agent
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Prepare state
        inputs = {"messages": st.session_state.messages}
        
        # Stream the execution
        full_response = ""
        with st.status("Thinking and Orchestrating...", expanded=True) as status:
            try:
                for event in agent_app.stream(inputs):
                    for key, value in event.items():
                        if key == "reasoner":
                            # Agent has produced a response (or tool call)
                            last_msg = value["messages"][-1]
                            if last_msg.tool_calls:
                                status.write(f"🛠️ Decided to call tools: {', '.join([tc['name'] for tc in last_msg.tool_calls])}")
                            else:
                                full_response = get_message_text(last_msg)
                        elif key == "tools":
                            # Tools have executed
                            status.write("✅ Tools executed successfully")
                            # Optionally show tool outputs
                            for msg in value["messages"]:
                                 status.write(f"📄 Tool Output: {msg.content[:200]}...")
                
                status.update(label="Complete!", state="complete", expanded=False)
            except Exception as e:
                status.update(label="Error Occurred", state="error", expanded=False)
                if "ResourceExhausted" in str(e) or "429" in str(e):
                    st.error("⚠️ API Rate Limit Exceeded. Please wait a minute and try again. (Google Gemini Free Tier Limit)")
                else:
                    st.error(f"An error occurred: {str(e)}")
        
        message_placeholder.markdown(full_response)
        st.session_state.messages.append(AIMessage(content=full_response))

# Footer
st.markdown("""
<div class="footer">
    ⚠️ <strong>Disclaimer:</strong> This is a demo application. All bookings are simulated. Prices and availability are estimates based on web search results.
</div>
""", unsafe_allow_html=True)
