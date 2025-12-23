from flask import Blueprint, request, jsonify
from backend.services.auth.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if UserService.get_user_by_email(email):
        return jsonify({'error': 'Email already registered'}), 400

    user = UserService.register_user(username, email, password)
    return jsonify({'message': 'User registered successfully', 'user_id': user.id})