import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain.agents import create_agent
load_dotenv()

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)

tavily_search_tool = TavilySearch(
    max_result=5,
    topic="general"
)

agent = create_agent(model, [tavily_search_tool])

user_input = "What nation hosted the Euro 2024? Include only wikipedia sources."

for step in agent.stream(
    {"messages": user_input},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()