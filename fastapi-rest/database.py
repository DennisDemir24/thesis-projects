#  en222yu
#  Database connection MongoDB FastAPI

import os
import motor.motor_asyncio
from model import Character

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
database = client.CharacterList
collection = database.character

async def fetch_one_character(id):
    document = await collection.find_one({"id": id})
    return document

# async def fetch_all_characters():
#     todos = []
#     cursor = collection.find({})
#     async for document in cursor:
#         todos.append(Character(**document))
#     return todos

# async def create_character(character):
#     document = character
#     result = await collection.insert_one(document)
#     return document


# async def update_character(id, desc):
#     await collection.update_one({"id": id}, {"$set": {"description": desc}})
#     document = await collection.find_one({"id": id})
#     return document

# async def remove_character(id):
#     await collection.delete_one({"id": id})
#     return True