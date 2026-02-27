import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model = init_chat_model("gpt-4.1")
print(model)

query = input("Enter the prompt? ")
response = model.invoke(query)

print(response)