from openai import OpenAI

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="how much is 2+3*23"
)

print(response.output_text)
