#en222yu

import strawberry

from fastapi import FastAPI, HTTPException
from strawberry.fastapi import GraphQLRouter
from pydantic import typing

from database import (
    #fetch_one_character,
    fetch_all_characters,
    # create_character,
    # update_character,
    # remove_character
)


@strawberry.type
class Character:
    id: str
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
    
    @strawberry.field
    def getCharacter(self, id: int) -> Character:
        characters = fetch_all_characters()

        for character in characters:
            if character.id == id:
                return character
        raise ValueError(f"No character with ID {id}")
    
    # @strawberry.field
    # def createCharacter(self, character: Character) -> Character:
    #     return create_character(character)
    
    # @strawberry.field
    # def updateCharacter(self, id: int, character: Character) -> Character:
    #     return update_character(id, character)
    
    # @strawberry.field
    # def deleteCharacter(self, id: int) -> str:
    #     remove_character(id)
    #     return f"Character with id {id} has been removed"
    
        
    # @strawberry.field
    # def hello(self) -> str:
    #     return "Hello World"

schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")