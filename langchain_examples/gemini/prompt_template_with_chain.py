from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, it looks for a .env file in the current directory
# You can also specify a path: load_dotenv(dotenv_path='path/to/.env')
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL')

llm = ChatGoogleGenerativeAI(
    model=model,
    temperature=0.7,#temperature controls how random or creative the LLM’s responses are.
    google_api_key=api_key
)

prompt = PromptTemplate.from_template(
    "Explain the following topic in simple terms: {topic}"
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"topic": "Vector Databases"})

print(result)