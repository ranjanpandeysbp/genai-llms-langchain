from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()
api_key = os.getenv('GROQ_API_KEY')
model = os.getenv('GEMINI_MODEL')

llm = ChatGroq(
    model=model,
    temperature=0.7,
    groq_api_key=api_key
)

response = llm.invoke("Explain LangChain in simple terms")

print(response.content)