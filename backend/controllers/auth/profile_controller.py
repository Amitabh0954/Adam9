from flask import Blueprint, request, jsonify
from backend.services.auth.profile_service import ProfileService

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id: int):
    user = ProfileService.get_profile(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'image_file': user.image_file})
    return jsonify({'error': 'User not found'}), 404

@profile_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id: int):
    data = request.json
    username = data.get('username')
    email = data.get('email')
    image_file = data.get('image_file')
    
    user = ProfileService.update_profile(user_id, username, email, image_file)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email, 'image_file': user.image_file})
    return jsonify({'error': 'User not found'}), 404