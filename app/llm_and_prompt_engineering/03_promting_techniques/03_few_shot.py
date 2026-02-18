from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

user_prompt = input("Enter the prompt: ")


few_shot_prompt = f"""
Classify the sentiment of the following sentences as "positive", "negative", or "neutral".

Example 1:
Sentence: "I absolutely love this product! It's amazing."
Sentiment: positive

Example 2:
Sentence: "The service was terrible and the staff was rude."
Sentiment: negative

Example 3:
Sentence: "I ordered a coffee and it was delivered on time."
Sentiment: neutral

Now, classify this sentence:
Sentence: {user_prompt}
Sentiment:"""

result = llm.invoke(few_shot_prompt)
print(result)

