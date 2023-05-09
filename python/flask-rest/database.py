import pymongo
import os
from model import Character

client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = client.RestThesisAPI
collection = db.characters

def fetch_one_character(id):
    document = collection.find_one({"id": int(id)})
    if document:
        return Character(**document)
    return None

def fetch_all_characters():
    characters = []
    cursor = collection.find({})
    for document in cursor:
        characters.append(Character(**document))
    return characters