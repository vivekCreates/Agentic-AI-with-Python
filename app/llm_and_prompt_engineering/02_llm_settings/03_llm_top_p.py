from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

top_p = float(input("Enter LLM Top_k: "))

llm = GoogleGenerativeAI(
     model=os.getenv("GEMINI_MODEL"),
     google_api_key=os.getenv("GOOGLE_API_KEY"),
     top_p=top_p,
     temperature=0.9,
     max_tokens=50
)

question = input("Enter you prompt: ")

response = llm.invoke(question)

print("Response", response)