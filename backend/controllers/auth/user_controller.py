from flask import Blueprint, request, jsonify
from backend.services.auth.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    try:
        user = UserService.register_user(email, password)
        return jsonify({'message': 'User registered successfully', 'user_id': user.id}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400