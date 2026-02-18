from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()


llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

instruction = "Answer the user's question politely and provide accurate information."

context = (
    "You are a virtual assistant for coding questions. Give the answers according to the question."
)
input_data = (
    "You can use the following resources to answer the question:\n"
    "1. Stack Overflow\n"
    "2. Google\n"
    "3. MDN Web Docs\n"
    "4. MDN Web Docs\n"
    "5. MDN Web Docs\n"
    "6. MDN Web Docs\n"
    "7. MDN Web Docs\n"
    "8. MDN Web Docs\n"
    "9. MDN Web Docs\n"
    "10. MDN Web Docs"
)
question = input("Enter prompt: ")

prompt = f"{instruction}\n\n{context}\n\n{input_data}\n\nUser's Question: {question}"

result = llm.invoke(prompt)

print(result)