# model.py
from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin: object 
    location: object 
    image: str 
    episodes: object 
    url: str
    created: str
