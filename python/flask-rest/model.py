# model.py
from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin: dict 
    location: dict 
    image: str 
    episodes: list 
    url: str
    created: str
