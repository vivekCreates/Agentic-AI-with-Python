from langchain_groq.chat_models import  ChatGroq
from langchain.messages import AIMessage,SystemMessage,HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)


# messages = [
#     SystemMessage("You are a helpful coding assistant. Who also write efficient code"),
#     HumanMessage("Write the binary search algorithm"),
#     AIMessage("Cherry blossoms bloom...")
# ]

ai_msg = AIMessage("I'd be happy to help you with that question!")


messages = [
    SystemMessage("You are a helpful assistant"),
    HumanMessage("Can you help me?"),
    ai_msg,
    HumanMessage("Great! What's 2+2?")
]

response = model.invoke(messages)

print(response.content)

