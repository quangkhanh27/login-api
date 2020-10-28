from ..extensions import db


def get_all_CTL():
    return [x for x in db.get_collection('login').find({})]

def get_by_id(id):
    return db.get_collection('login').find_one({"_id":id})

def add_CTL(obj):
    return db.get_collection('login').insert(obj)

def delete_CTL(id):
    return db.get_collection('login').find_one_and_delete({"_id":id})

def update_CLT(todo):
    return db.get_collection('login').find_one_and_update({"_id":todo['_id']},{"$set":todo})