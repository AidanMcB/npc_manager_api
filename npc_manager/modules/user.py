from flask import Blueprint, jsonify, request
from npc_manager.database import db
from npc_manager.models.user import User  # Import your User model

blueprint = Blueprint('user', __name__)  # Create a blueprint instance

@blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # Get all users from the database
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at,
        }
        user_list.append(user_data)
    
    return jsonify(user_list)  # Return the user list as JSON

@blueprint.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):
    user = User.get_by_username(username)  # Use the method from your model
    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at,
        }
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404
    
@blueprint.route('/users/id/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id) # Use SQLAlchemy's get method to fetch the user by id
    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at,
        }
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found, couldn't find user by ID"}), 404


@blueprint.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    created_at = data.get('created_at')
    
    user = User(username=username, created_at=created_at)
    if user.register_user_if_not_exist():
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "User registration failed"}), 400
