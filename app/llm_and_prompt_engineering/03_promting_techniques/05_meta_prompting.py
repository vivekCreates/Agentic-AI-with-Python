from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = GoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


meta_prompt = """
Your task is to create a better prompt for solving math word problems. The prompt should guide the model to break down the problem into clear, logical steps and provide the final answer.

Write a prompt that would help the model solve this problem step by step. Be clear and concise.
"""


generated_prompt = llm.invoke(meta_prompt)
print("Generated Prompt:\n", generated_prompt)

problem = "Sarah has 15 apples. She gives 4 apples to her friend and then buys 10 more apples from the store. How many apples does Sarah have now?"

final_prompt = f"{generated_prompt}\n\nProblem: {problem}"

result = llm.invoke(final_prompt)
print("\nTest Result:\n", result)