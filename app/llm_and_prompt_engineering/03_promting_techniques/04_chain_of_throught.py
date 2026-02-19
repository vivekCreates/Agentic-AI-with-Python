from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os


load_dotenv()


llm = GoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

cot_prompt = """
Solve the following math problem step by step:

Problem: A bakery sells 15 cupcakes in the morning and 20 cupcakes in the afternoon. Each cupcake costs $2. How much money did the bakery make in total?

Step 1: Calculate the total number of cupcakes sold.
- Morning cupcakes: 15
- Afternoon cupcakes: 20
- Total cupcakes sold = 15 + 20 = 35

Step 2: Calculate the total revenue.
- Price per cupcake: $2
- Total revenue = Total cupcakes sold * Price per cupcake
- Total revenue = 35 * 2 = $70

Final Answer: The bakery made $70 in total.
"""

result = llm.invoke(cot_prompt)

print(result)