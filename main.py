import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=api_key
)

history = []

def ask(question):
  question_msg = {
    'role': 'user',
    'content': question,
  }
  history.append(question_msg)
  response = client.chat.completions.create(
    messages=history,
    model='gpt-3.5-turbo',
  )
  answer_msg = response.choices[0].message
  history.append(answer_msg)
  return answer_msg.content

while(True):
  question = input("Question: ")
  if(question.strip() == ''):
    break
  answer = ask(question)
  print('\n')
  print(f"Answer: {answer}")
  print('\n')

print("Bye.")
