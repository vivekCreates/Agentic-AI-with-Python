import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()
os.environ["USER_AGENT"] = os.getenv("USER_AGENT")

api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

url = "https://www.apple.com/in/",


docs = WebBaseLoader(url).load()




template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an ai agent that tell about the websites"),
        ("human", "{data}"),
        ("human","What is the price of IPhone 17? ")
    ]
)

model = ChatGroq(
    model=model_name,
    api_key=api_key
)

prompt = template.format_messages(data=docs[0].page_content)


result = model.invoke(prompt)

print(result.content)