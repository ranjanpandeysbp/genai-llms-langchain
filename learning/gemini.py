from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL')

def get_health_advice(query):
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model=model,
        config=types.GenerateContentConfig(
        system_instruction="You are an expert in software architecture and design. Your name is VirtualArchitect."),
        contents=query
    )
    return response.text

if __name__ == "__main__":
    user_prompt = input("Enter your requirement: ")
    advice = get_health_advice(user_prompt)
    print("Architecture Advice:")
    print(advice)