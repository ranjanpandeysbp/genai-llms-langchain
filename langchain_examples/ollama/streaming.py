from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen3:0.6b")

for chunk in llm.stream("Write a short poem about AI"):
    print(chunk, end="", flush=True)