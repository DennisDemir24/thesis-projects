#  en222yu
#  Database connection MongoDB Flask

import pymongo
import os
from model import Character

client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = client.RestThesisAPI
collection = db.characters


def fetch_one_character(id):
     document = collection.find_one({"id": id})
     del document['_id']  # Remove the _id field
     character = Character(**document)
     return character

def fetch_all_characters():
    characters = []
    cursor = collection.find({})
    for document in cursor:
        del document['_id']  # Remove the _id field
        characters.append(Character(**document))
    return characters
