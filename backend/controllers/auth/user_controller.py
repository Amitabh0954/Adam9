from flask import Blueprint, request, jsonify, session
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

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = UserService.authenticate_user(email, password)
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully', 'user_id': user.id}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/password-reset', methods=['POST'])
def password_reset_request():
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    try:
        UserService.send_password_reset_email(email)
        return jsonify({'message': 'Password reset email sent'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/password-reset/<token>', methods=['POST'])
def password_reset(token):
    data = request.json
    new_password = data.get('new_password')

    if not new_password:
        return jsonify({'error': 'New password is required'}), 400

    try:
        UserService.reset_password(token, new_password)
        return jsonify({'message': 'Password reset successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400