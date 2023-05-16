#  en222yu

from typing import List
from pydantic import BaseModel

class Origin(BaseModel):
    name: str
    url: str


class Location(BaseModel):
    name: str
    url: str

class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin: Origin 
    location: Location 
    image: str 
    episode: List[str]
    url: str
    created: str

