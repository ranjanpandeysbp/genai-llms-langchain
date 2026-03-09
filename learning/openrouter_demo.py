from openai import OpenAI

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

completion = client.chat.completions.create(
  model="openai/gpt-5.2",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

print(completion.choices[0].message.content)
