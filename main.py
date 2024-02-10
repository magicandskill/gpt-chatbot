import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api_key
)

response = client.chat.completions.create(
  messages=[
    {
      "role": "user",
      "content": "what is programming?",
    }
  ],
  model="gpt-3.5-turbo",
)

print(response)
