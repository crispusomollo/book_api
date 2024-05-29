from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()

class User:
    @staticmethod
    def create_user(data):
        data['password'] = generate_password_hash(data['password'])
        return mongo.db.users.insert_one(data)
    
    @staticmethod
    def get_user(username):
        return mongo.db.users.find_one({"username": username})
    
    @staticmethod
    def update_user(username, data):
        return mongo.db.users.update_one({"username": username}, {"$set": data})
    
    @staticmethod
    def delete_user(username):
        return mongo.db.users.delete_one({"username": username})

