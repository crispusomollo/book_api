from flask import Flask, jsonify, request
from os import getenv
from markupsafe import escape
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId, InvalidId

app = Flask(__name__)

# Configure the MongoDB database
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookapi"
mongo = PyMongo(app)

@app.route('/')
def hello():
    name = request.args.get("name", "Simple Book API")
    return f'Welcome to my, {escape(name)}!'

# Route to fetch all documents in a collection
@app.route('/get_items', methods=['GET'])
def get_items():
    items = mongo.db.books.find()
    return dumps(items)

# Validate ObjectId
def is_valid_objectid(id):
    try:
        ObjectId(id)
        return True
    except InvalidId:
        return False

@app.route('/get_item/<id>', methods=['GET'])
def get_item(id):
    if not is_valid_objectid(id):
        return jsonify({"error": "Invalid ID format"}), 400
    item = mongo.db.books.find_one({'_id': ObjectId(id)})
    if item is None:
        return jsonify({"error": "Book not found"}), 404
    return dumps(item)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_data = request.json
    # Sanitize input data
    sanitized_data = {k: v for k, v in item_data.items() if k in ['title', 'author']}  # Allow only specific fields
    mongo.db.books.insert_one(sanitized_data)
    return jsonify(message="Book added successfully"), 201

# Route to fetch all documents in a collection
@app.route('/get_users', methods=['GET'])
def get_users():
    items = mongo.db.users.find()
    return dumps(items)

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
    item = mongo.db.users.find_one({'_id': ObjectId(id)})
    if item is None:
        return jsonify({"error": "User not found"}), 404
    return dumps(item)

@app.route('/add_user', methods=['POST'])
def add_user():
    item_data = request.json
    # Sanitize input data
    sanitized_data = {k: v for k, v in item_data.items() if k in ['name', 'email']}  # Allow only specific fields
    mongo.db.users.insert_one(sanitized_data)
    return jsonify(message="User added successfully"), 201

@app.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
