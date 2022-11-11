from fastapi import APIRouter
from database.mongodb import db

from bson import json_util
from json import loads

router = APIRouter()

@router.get("/q")
def get_penguins():
        res = list(db["penguin_size"].find({}))[:5]
        return loads(json_util.dumps(res))