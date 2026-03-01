import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import HumanMessage

load_dotenv()

model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(
    model=model_name,
    api_key=os.getenv("GROQ_API_KEY")
)

agent = create_agent(
    model=model,
    checkpointer=InMemorySaver(),
    middleware=[
        SummarizationMiddleware(
            model=model,  
            trigger=("messages", 10),
            keep=("messages", 4),
        ),
    ],
)

ques = [
  "What is 2 + 2?",
  "What is 10 - 3?",
  "What is 5 × 6?",
  "What is 20 ÷ 4?",
  "What is 9 + 8 - 3?"
]

config = {
    "configurable": {"thread_id": "1"}
}

for q in ques:
    response = agent.invoke(
        {"messages": [HumanMessage(content=q)]}, 
        config=config
    )
    print(response)