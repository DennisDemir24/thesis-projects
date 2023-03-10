#  en222yu
#  Database connection MongoDB FastAPI

import pymongo
import os
from model import Character

client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = client.RestThesisAPI
collection = db.characters


def fetch_one_character(id):
    document = collection.find_one({"id": int(id)})
    print(document)
    return document

def fetch_all_characters(): 
    characters = []
    cursor = collection.find({})
    for document in cursor:
        characters.append(Character(**document))
    return characters

def create_character(character):
    document = character
    result = collection.insert_one(document)
    return document

def update_character(id, status, image, url):
    collection.update_one(
        {"id": int(id)}, 
        {"$set": {"status": status, "image": image, "url": url}},
        upsert=True
        )
    document = collection.find_one({"id": int(id)})
    return document

def remove_character(id):
    collection.delete_one({"id": int(id)})
    return True