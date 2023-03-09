#  en222yu
#  Database connection MongoDB FastAPI

import pymongo
import os

client = pymongo.MongoClient(os.environ['MONGO_URI'])
db = client.RestThesisAPI
collection = db.characters