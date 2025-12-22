from flask import Blueprint, request, jsonify
from backend.services.auth.profile_service import ProfileService

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/update', methods=['PUT'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    try:
        user = ProfileService.update_profile(user_id, username, email, password)
        return jsonify({"message": "Profile updated successfully", "user": user.username}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400