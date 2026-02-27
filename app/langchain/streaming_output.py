from langchain_groq.chat_models import  ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)
prompt = input("Enter the prompt: ")

# for chunk in model.stream(prompt):
#     print(chunk.text, end="|", flush=True)

for chunk in model.stream(prompt):
    print(chunk.text,end=" ")

