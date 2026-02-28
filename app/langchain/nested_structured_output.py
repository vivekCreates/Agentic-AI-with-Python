import os
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from typing import List
from dotenv import load_dotenv


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)

class Actor(BaseModel):
    name:str=Field(...,description="Name of actor")
    age:int=Field(...,description="Age of actor")


class MovieDetail(BaseModel):
    title:str=Field(...,description="Title of the movie")
    year:str=Field(...,description="Year of the movie")
    cast:List[Actor] = Field(...,description="Cast of the movie")
    director:str=Field(...,description="Director of the movie")
    budget:float=Field(...,description="Budget of the movie")
    profit:float=Field(...,description="Profit of the movie")
    
    
model_with_structure = model.with_structured_output(MovieDetail)

prompt = input("Enter movie name: ")

response = model_with_structure.invoke(prompt)

print(response)