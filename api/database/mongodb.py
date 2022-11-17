from fastapi import APIRouter
from pymongo import MongoClient
from bson import json_util
from json import loads
from config import URL

client = MongoClient(URL)
db = client.get_database("penguin_data")

def find_collection(collection, filter ={}, project ={}):
    return db[collection].find(filter, project)


def paginate(page=0, per_page=100):
    def x(mongodb_cursor):
        data= mongodb_cursor.limit(per_page).skip(per_page*page)
        return { "page": page,
            "results": loads(json_util.dumps(data)) 
        }
    return x

