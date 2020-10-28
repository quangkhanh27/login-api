from flask_pymongo import pymongo
from app.settings import MONGO_URI

# mongo = new MongoClient(MONGO_URI)

# MONGO_URI='mongodb+srv://login:lamquangkhanh@cluster0.7ubsg.mongodb.net/login?retryWrites=true&w=majority'

mongo = pymongo.MongoClient(MONGO_URI)

db = mongo.get_database('login')