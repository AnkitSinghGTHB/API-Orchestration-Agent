import os
from dotenv import load_dotenv

# Try loading from default location (current directory)
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    print(f"API Key found: {api_key[:5]}...{api_key[-5:]}")
    print(f"Length: {len(api_key)}")
else:
    print("API Key NOT found in environment variables.")

# Check if .env file exists
if os.path.exists(".env"):
    print(".env file exists in current directory.")
else:
    print(".env file does NOT exist in current directory.")
