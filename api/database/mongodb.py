from fastapi import APIRouter
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("url"))
db = client.get_database("penguin_data")

