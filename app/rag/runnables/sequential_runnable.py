import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)


model = ChatGroq(model=model_name)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)