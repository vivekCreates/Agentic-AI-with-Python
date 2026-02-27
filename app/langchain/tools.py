from langchain_groq.chat_models import  ChatGroq
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

@tool
def get_weather(location:str):
    """Get weather at the location"""
    return f"{location} weather is very sunny"


model = ChatGroq(model=model_name)
model_with_tool = model.bind_tools([get_weather])


messages = [{"role":"user","content":"What's the weather of bulandshahr? "}]
ai_response = model_with_tool.invoke(messages)
messages.append(ai_response)

for tool_call in ai_response.tool_calls:
    tool_res = get_weather.invoke(tool_call)
    messages.append(tool_res)
    


final_result = model_with_tool.invoke(messages)
print(final_result.text)