#en222yu

import strawberry

from fastapi import FastAPI, HTTPException
from strawberry.fastapi import GraphQLRouter
from pydantic import typing
from performance import PerformanceMiddleware

from database import (
    fetch_one_character,
    fetch_all_characters
)

@strawberry.type
class Origin:
    name: str
    url: str

@strawberry.type
class Location:
    name: str
    url: str

@strawberry.type
class Character:
    id: str
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin: Origin
    location: Location
    image: str 
    episode: typing.List[str]
    url: str
    created: str
    

@strawberry.type
class Query:
    @strawberry.field
    def characters(self) -> typing.List[Character]:
        response = fetch_all_characters()
        return response
    
    @strawberry.field
    def getCharacter(self, id: int) -> Character:
        response = fetch_one_character(id)
        if response:
            return response
        raise ValueError(f"No character with ID {id}")
    
schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
# Add performance middleware
app.add_middleware(PerformanceMiddleware)

app.include_router(graphql_app, prefix="/graphql")