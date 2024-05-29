from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    User.create_user(data)
    return jsonify({"message": "User created successfully"}), 201

@user_bp.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = User.get_user(username)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/users/<username>', methods=['PUT'])
def update_user(username):
    data = request.get_json()
    User.update_user(username, data)
    return jsonify({"message": "User updated successfully"}), 200

@user_bp.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    User.delete_user(username)
    return jsonify({"message": "User deleted successfully"}), 200

