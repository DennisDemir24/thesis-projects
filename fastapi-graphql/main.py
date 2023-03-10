import strawberry

from fastapi import FastAPI, HTTPException
from strawberry.fastapi import GraphQLRouter
from pydantic import typing

from database import (
    fetch_one_character,
    fetch_all_characters,
    create_character,
    update_character,
    remove_character,
)


@strawberry.type
class Character:
    id: int
    name: str
    status: str
    species: str
    type: str 
    gender: str 
    origin:  typing.List[str] 
    location: typing.List[str]  
    image: str 
    episodes: typing.List[str]
    url: str
    created: str

@strawberry.type
class Query:
    @strawberry.field
    def characters(self) -> typing.List[Character]:
        response = fetch_all_characters()
        return response
    
    # @strawberry.field
    # def hello(self) -> str:
    #     return "Hello World"

schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")