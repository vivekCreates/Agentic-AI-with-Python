from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5 # 0.0 to 1.0 randomise the output
)

query = input("Ask a question: ")

result = llm.invoke(query)
print(result)