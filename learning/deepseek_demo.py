from openai import OpenAI

client = OpenAI(api_key="sk-55fde1f72d204975937c28065b0f8015", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Capital of India?"},
    ],
    stream=False
)

print(response.choices[0].message.content)