import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api_key
)

def ask(question):
  response = client.chat.completions.create(
    messages=[
      {
          'role': 'user',
          'content': question,
      }
    ],
    model='gpt-3.5-turbo',
  )
  return response.choices[0].message.content

while(True):
  question = input("Question: ")
  if(question.strip() == ''):
    break
  answer = ask(question)
  print('\n')
  print(f"Answer: {answer}")
  print('\n')

print("Bye.")
