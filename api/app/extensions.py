from flask_pymongo import pymongo

MONGO_URI='mongodb+srv://login:lamquangkhanh@cluster0.7ubsg.mongodb.net/login?retryWrites=true&w=majority'

mongo = pymongo.MongoClient(MONGO_URI)

db = mongo.get_database('login')