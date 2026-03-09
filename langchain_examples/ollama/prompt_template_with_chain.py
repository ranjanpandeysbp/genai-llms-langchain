from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LLM
llm = OllamaLLM(
    model='qwen3:0.6b',
    base_url="http://localhost:11434"
)

# Prompt template
prompt = PromptTemplate.from_template(
    "Explain the following topic in simple terms: {topic} {sample_input}"
)

# Chain
chain = prompt | llm | StrOutputParser()

# Run
result = chain.invoke({"topic": "Vector Databases", "sample_input": "Give example of popular vector databases?"})

print(result)