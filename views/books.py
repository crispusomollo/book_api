from flask import Blueprint, request, jsonify
from models.models import mongo, Book

books = Blueprint('books', __name__)

@books.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(data['title'], data['author'], data['user_id'])
    mongo.db.books.insert_one(new_book.to_dict())
    return jsonify({"message": "Book created successfully"}), 201

@books.route('/books/<title>', methods=['GET'])
def get_book(title):
    book = mongo.db.books.find_one({"title": title})
    if book:
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

