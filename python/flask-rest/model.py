# model.py
from pydantic import BaseModel
from typing import List

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
    episode: List[str] 
    url: str
    created: str
