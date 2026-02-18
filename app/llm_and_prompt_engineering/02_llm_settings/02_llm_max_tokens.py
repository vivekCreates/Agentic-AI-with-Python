from langchain_google_genai import GoogleGenerativeAI
from os import getenv
from dotenv import load_dotenv
load_dotenv()


llm = GoogleGenerativeAI(
    model=getenv("GEMINI_MODEL"),
    google_api_key=getenv("GOOGLE_API_KEY"),
    max_tokens=100,
    temperature=0.9
    )

query = input("Ask a question: ")

result = llm.invoke(query)
print(result)