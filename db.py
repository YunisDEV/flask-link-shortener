from pymongo import MongoClient
import os

client = MongoClient(os.environ.get(
    "LS_DATABASE", "mongodb://localhost:27017/"))

db = client['link_shortener']

col = db['links']
