import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from src.agent import app

load_dotenv()

def main():
    print("✈️ AI Travel Agent CLI")
    print("Type 'quit' to exit.")
    
    messages = []
    
    def get_message_text(content):
        if isinstance(content, list):
            return "".join([part.get("text", "") for part in content if isinstance(part, dict)])
        return content
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
            
        messages.append(HumanMessage(content=user_input))
        
        print("\nAgent is thinking...")
        inputs = {"messages": messages}
        
        final_response = ""
        for event in app.stream(inputs):
            for key, value in event.items():
                if key == "reasoner":
                    last_msg = value["messages"][-1]
                    if last_msg.tool_calls:
                        print(f"🛠️  Calling tools: {', '.join([tc['name'] for tc in last_msg.tool_calls])}")
                    else:
                        final_response = get_message_text(last_msg.content)
                elif key == "tools":
                    print("✅ Tools executed.")
        
        print(f"\nAgent: {final_response}")
        messages.append(HumanMessage(content=final_response))

if __name__ == "__main__":
    main()
