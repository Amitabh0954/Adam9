from flask import Blueprint, request, jsonify, session
from backend.services.auth.user_service import UserService

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user_email = session.get('user_email')
    if not user_email:
        return jsonify({'error': 'Unauthorized access'}), 401

    user = UserService.get_user_by_email(user_email)
    if user:
        return jsonify({'username': user.username, 'email': user.email}), 200
    return jsonify({'error': 'User not found'}), 404

@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_email = session.get('user_email')
    if not user_email:
        return jsonify({'error': 'Unauthorized access'}), 401
    
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        user = UserService.update_user_profile(user_email, username, email)
        return jsonify({'message': 'Profile updated successfully', 'username': user.username, 'email': user.email}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400