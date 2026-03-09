from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(
    model='qwen3:0.6b', 
    base_url="http://localhost:11434",
    reasoning=False
)

# Send a prompt
response = llm.invoke("Explain LangChain in simple terms")

print(response)