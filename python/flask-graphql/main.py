import graphene
from flask import Flask
from flask_graphql import GraphQLView
from model import Character
from performance import PerformanceMiddleware

from database import (
    fetch_one_character,
    fetch_all_characters
)

class Character(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    status = graphene.String()
    species = graphene.String()
    type = graphene.String()
    gender = graphene.String()
    origin = graphene.List(graphene.String)
    location = graphene.List(graphene.String)
    image = graphene.String()
    episode = graphene.List(graphene.String)
    url = graphene.String()
    created = graphene.String()


class Query(graphene.ObjectType):
    characters = graphene.List(Character)
    def resolve_characters(self, info):
        response = fetch_all_characters()
        return response
    
    character = graphene.Field(Character, id=graphene.Int(required=True))

    def resolve_character(self, info, id):
        response = fetch_one_character(id)
        if response:
            return response
        raise ValueError(f"No character with ID {id}")


schema = graphene.Schema(query=Query)

app = Flask(__name__)

app.add_url_rule('/graphql', 
                view_func=GraphQLView.as_view('graphql', 
                schema=schema,
                graphiql=True))

app.wsgi_app = PerformanceMiddleware(app.wsgi_app)

if __name__ == "__main__":
    app.run(debug=True)