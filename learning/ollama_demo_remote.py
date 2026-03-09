from ollama import Client

# 1. Initialize the client with your remote server's IP or domain
# Make sure to include the port (default is 11434)
client = Client(host='http://localhost:11434')

# 2. Use client.chat instead of the global chat function
response = client.chat(
    model='qwen3:0.6b', 
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful Health Coach.',
        },
        {
            'role': 'user',
            'content': 'I am a software engineer, how can I keep myself fit?',
        },
    ]
)

# 3. Access the response as usual
print(response.message.content)