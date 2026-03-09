from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a python code to find the factorial of a number."
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)