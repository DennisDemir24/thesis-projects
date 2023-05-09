#  en222yu

from typing import List
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
    episode: List[str]
    url: str
    created: str

