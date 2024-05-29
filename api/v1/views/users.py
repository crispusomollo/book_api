# book_api/api/v1/views/books.py

from flask import Blueprint, request, jsonify
from models.book import Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.get_all_books()
    return jsonify(books), 200

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@books_bp.route('/books', methods=['POST'])
def add_book():
    book_data = request.get_json()
    Book.add_book(book_data)
    return jsonify({"message": "Book added successfully"}), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    update_data = request.get_json()
    result = Book.update_book(book_id, update_data)
    if result.matched_count:
        return jsonify({"message": "Book updated successfully"}), 200
    return jsonify({"error": "Book not found"}), 404

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = Book.delete_book(book_id)
    if result.deleted_count:
        return jsonify({"message": "Book deleted successfully"}), 200
    return jsonify({"error": "Book not found"}), 404

