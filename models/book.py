from flask_pymongo import PyMongo

mongo = PyMongo()

class Book:
    @staticmethod
    def create_book(data):
        return mongo.db.books.insert_one(data)
    
    @staticmethod
    def get_book(book_id):
        return mongo.db.books.find_one({"_id": book_id})
    
    @staticmethod
    def update_book(book_id, data):
        return mongo.db.books.update_one({"_id": book_id}, {"$set": data})
    
    @staticmethod
    def delete_book(book_id):
        return mongo.db.books.delete_one({"_id": book_id})

