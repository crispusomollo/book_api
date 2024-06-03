# book_api/api/v1/views/books.py

from flask import Blueprint, request, jsonify
from models.book import Book

book_bp = Blueprint('book', __name__)

@book_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    Book.create_book(data)
    return jsonify({"message": "Book created successfully"}), 201

@book_bp.route('/get_books', methods=['GET'])
def get_book(book_id):
    book = Book.get_book(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

@book_bp.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    Book.update_book(book_id, data)
    return jsonify({"message": "Book updated successfully"}), 200

@book_bp.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    Book.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"}), 200

