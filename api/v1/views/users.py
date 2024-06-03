from flask import Blueprint, request, jsonify
from models.models import mongo, User

users = Blueprint('users', __name__)

@users.route('/get_users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data['username'], data['email'])
    mongo.db.users.insert_one(new_user.to_dict())
    return jsonify({"message": "User created successfully"}), 201

@users.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = mongo.db.users.find_one({"username": username})
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404
