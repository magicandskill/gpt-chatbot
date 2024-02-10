import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(
  api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

while(True):
  question = input("Question: ")
  if(question.strip() == ''):
    break
  response = chat.send_message(question)
  print('\n')
  print(f"Answer: {response.text}")
  print('\n')

print("Bye.")
