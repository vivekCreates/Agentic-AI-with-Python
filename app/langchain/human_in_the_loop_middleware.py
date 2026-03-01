import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.types import Command
load_dotenv()



os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)

def read_email_tool(email_id: str) -> str:
    """Mock function to read an email by its ID."""
    return f"Email content for ID: {email_id}"

def send_email_tool(recipient: str, subject: str, body: str) -> str:
    """Mock function to send an email."""
    return f"Email sent to {recipient} with subject '{subject}'"

agent = create_agent(
    model=model,
    tools=[read_email_tool, send_email_tool],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "send_email_tool": {
                    "allowed_decisions": ["approve", "edit", "reject"],
                },
                "read_email_tool": False,
            }
        ),
    ],
)

config = {
    "configurable":{
        "thread_id":"1"
    }
}

response = agent.invoke({"messages":[HumanMessage("send email to one@example.com from v@example.com that you are a great software engineer")]},config=config)

if "__interrupt__" in response:
    print("approving")
    
    response = agent.invoke(
        Command(
            resume={
                "decisions":[
                    {"type":"approve"}
                ]
            }
        ),
        config=config
    )

print(response)