from langchain_ollama import OllamaLLM
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama  # use Chat variant for system prompts

llm = ChatOllama(
    model='qwen3:0.6b',
    base_url="http://31.97.237.200:11434",
)

messages = [
    SystemMessage(content="You are a helpful assistant. Always respond in English."),
    HumanMessage(content="Explain LangChain in simple terms")
]

response = llm.invoke(messages)
print(response.content)