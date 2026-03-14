import warnings
warnings.filterwarnings("ignore")  # Suppress LangGraph deprecation warnings

from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent  # works in your env

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "false"

model = os.getenv('OLLAMA_MODEL', 'llama3.2')
ollama_base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')

@tool
def multiply_numbers(input: str) -> int:
    """Multiply two numbers. Input must be two numbers separated by a comma, e.g. '6,7'"""
    a, b = input.strip().split(",")
    return int(a.strip()) * int(b.strip())

llm = ChatOllama(
    model=model,
    temperature=0,
    base_url=ollama_base_url
)

tools = [multiply_numbers]

agent = create_react_agent(llm, tools)

result = agent.invoke({"messages": [{"role": "user", "content": "What is 6 multiplied by 7?"}]})

print(result["messages"][-1].content)