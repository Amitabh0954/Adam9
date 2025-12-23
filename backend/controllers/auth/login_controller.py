from flask import Blueprint, request, jsonify, session
from backend.services.auth.user_service import UserService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400

    if UserService.verify_user(email, password):
        session['user_email'] = email
        return jsonify({'message': 'Login successful'})

    return jsonify({'error': 'Invalid email or password'}), 401

@login_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)
    return jsonify({'message': 'Logout successful'})