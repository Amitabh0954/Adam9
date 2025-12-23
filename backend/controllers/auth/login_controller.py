from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from backend.repositories.auth.user_repository import UserRepository
from backend.services.auth.session_service import SessionService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user = UserRepository.get_user_by_email(email)
    if user and check_password_hash(user.password, password):
        session = SessionService.create_session(user.id)
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'token': session.token})
    return jsonify({'error': 'Invalid credentials'}), 401