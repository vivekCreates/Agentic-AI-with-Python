import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("GEMINI_MODEL")

model = ChatGoogleGenerativeAI(model=model_name)
prompt = input("Enter the prompt: ")


response = model.invoke(prompt)

print(response)