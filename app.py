from flask import Flask, jsonify, request
from os import getenv
from markupsafe import escape
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId, InvalidId

from flask import Flask
from views.users import users
from views.books import books
from config.settings import Config

#app = Flask(__name__)
#app.config.from_object(Config)

app = Flask(__name__)

# Configure the MongoDB database
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookapi"
mongo = PyMongo(app)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# Route to fetch all documents in a collection
@app.route('/get_books', methods=['GET'])
def get_books():
    items = mongo.db.books.find()
    return dumps(items)

# Validate ObjectId
def is_valid_objectid(id):
    try:
        ObjectId(id)
        return True
    except InvalidId:
        return False

@app.route('/get_book/<id>', methods=['GET'])
def get_book(id):
    if not is_valid_objectid(id):
        return jsonify({"error": "Invalid ID format"}), 400
    item = mongo.db.books.find_one({'_id': ObjectId(id)})
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return dumps(item)

@app.route('/add_book', methods=['POST'])
def add_book():
    item_data = request.json
    # Sanitize input data
    sanitized_data = {k: v for k, v in item_data.items() if k in ['name', 'email']}  # Allow only specific fields
    mongo.db.books.insert_one(sanitized_data)
    return jsonify(message="Item added successfully"), 201

# Route to fetch all users in a collection
@app.route('/get_users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return dumps(users)

# Validate ObjectId
def is_valid_objectid(id):
    try:
        ObjectId(id)
        return True
    except InvalidId:
        return False

@app.route('/get_user/<id>', methods=['GET'])
def get_user(id):
    if not is_valid_objectid(id):
        return jsonify({"error": "Invalid ID format"}), 400
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user is None:
        return jsonify({"error": "Item not found"}), 404
    return dumps(user)

@app.route('/add_user', methods=['POST'])
def add_item():
    item_data = request.json
    # Sanitize input data
    sanitized_data = {k: v for k, v in item_data.items() if k in ['name', 'email']}  # Allow only specific fields
    mongo.db.users.insert_one(sanitized_data)
    return jsonify(message="Item added successfully"), 201

@books.route('/users/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    # Find the book by title
    book = mongo.db.users.find_one({"id": id})
    if book:
        # Update the book with new data
        mongo.db.users.update_one({"username": username}, {"$set": data})
        return jsonify({"message": "Book updated successfully"}), 200
    return jsonify({"message": "Book not found"}), 404

@users.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({"username": username})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5002", debug=True)

