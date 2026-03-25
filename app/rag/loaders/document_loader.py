from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

data = TextLoader("app/rag/notes.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an ai agent that summarizes the text"),
        ("human", "{data}")
    ]
)

model = ChatGroq(
    model=model_name,
    api_key=api_key
)

prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)

print(result.content)