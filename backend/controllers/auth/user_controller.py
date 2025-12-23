from flask import Blueprint, request, jsonify
from backend.services.auth.user_service import UserService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    user = UserService.register_user(username, email, password)
    return jsonify({'id': user.id, 'username': user.username, 'email': user.email})