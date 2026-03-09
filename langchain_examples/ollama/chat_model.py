from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

chat = ChatOllama(
    model="qwen3:0.6b",
    base_url="http://localhost:11434"
)

response = chat.invoke([
    HumanMessage(content="What is Retrieval Augmented Generation?")
])

print(response.content)