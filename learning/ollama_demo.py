from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='qwen3:0.6b', messages=[
  {
    'role': 'user',
    'content': 'write a python script to print hello world',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)