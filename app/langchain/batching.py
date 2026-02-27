from langchain_groq.chat_models import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)

responses = model.batch(
    [
        "What is superstitions",
        "Why do we belives",
        "What is Jiddu krishanmurti's philosphy",
    ]
)

for response in responses:
    print(response)
