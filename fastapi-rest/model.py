#  en222yu

# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel

class Character(BaseModel):
    title: str
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin: object 
    location: object 
    image: str 
    episodes: list
    url: str