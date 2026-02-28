import os
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("GROQ_MODEL")

model = ChatGroq(model=model_name)

class Movie(BaseModel):
    title:str=Field("Title of the movie")
    year:str=Field("Year of the movie")
    director:str=Field("Director of the movie")
    rating:float=Field("Ratings of the movie")

model_with_structure = model.with_structured_output(Movie)

prompt = input("Enter prompt: ")
response = model_with_structure.invoke(prompt)

print(response)