import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    api_key=os.getenv("GROQ_API_KEY"),
)

agent = create_agent(
    model,
    checkpointer=InMemorySaver(),
)

config = {
    "configurable":{"thread_id":"1"}
}

response = agent.invoke(
    {"messages": [HumanMessage(content="Hello, My name is Vivek")]},
    config=config,
)

ans = agent.invoke(
    {
        "messages":[HumanMessage(content="What is my name ?")],
    }, config=config
)

print(ans)