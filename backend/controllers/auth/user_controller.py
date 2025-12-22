from flask import Blueprint, request, jsonify
from backend.services.auth.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    try:
        user = UserService.register_user(username, email, password)
        return jsonify({"message": "User registered successfully", "user": user.username}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400