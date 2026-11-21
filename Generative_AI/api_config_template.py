import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai #import the gemini genai module
from google.genai import types

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


if os.getenv("GEMINI_API_KEY"):
    print("Gemini API key loaded successfully!")
else:
    print("Gemini API key not found!")

MODEL_NAME = "gemini-3.5-flash-lite"
# connect to the Gemini API using the API key from the .env file
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(
        timeout=15000,
        retry_options=types.HttpRetryOptions(attempts=1)
    )
)