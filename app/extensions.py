from flask_pymongo import pymongo
from app.settings import MONGO_URI

mongo = pymongo.MongoClient(MONGO_URI)

db = mongo.get_database('login')