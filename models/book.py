# book_api/models/book.py

from pymongo import MongoClient
from config.settings import config

client = MongoClient(config.MONGO_URI)
db = client.get_database()
books_collection = db.books

class Book:
    @staticmethod
    def get_all_books():
        return list(books_collection.find({}, {"_id": 0}))

    @staticmethod
    def get_book_by_id(book_id):
        return books_collection.find_one({"id": book_id}, {"_id": 0})

    @staticmethod
    def add_book(book_data):
        return books_collection.insert_one(book_data)

    @staticmethod
    def update_book(book_id, update_data):
        return books_collection.update_one({"id": book_id}, {"$set": update_data})

    @staticmethod
    def delete_book(book_id):
        return books_collection.delete_one({"id": book_id})

