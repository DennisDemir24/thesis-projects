import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Character:
    id: int
    name: str
    # status: str
    # species: str
    # type: str 
    # gender: str 
    # origin: object 
    # location: object 
    # image: str 
    # episodes: object
    # url: str
    # created: str

@strawberry.type
class Query:
    @strawberry.field
    def character(self) -> Character:
        return Character(id=1, name="Rick")

schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")