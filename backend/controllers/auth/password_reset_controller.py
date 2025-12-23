from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/reset-password', methods=['POST'])
def request_password_reset():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    user = UserService.get_user_by_email(email)
    if not user:
        return jsonify({'error': 'Invalid email'}), 400

    PasswordResetService.send_reset_email(email)
    return jsonify({'message': 'Password reset link sent'}), 200

@reset_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.json
    new_password = data.get('new_password')

    if not new_password:
        return jsonify({'error': 'New password is required'}), 400

    email = PasswordResetService.confirm_reset_token(token)
    if not email:
        return jsonify({'error': 'Invalid or expired token'}), 400

    PasswordResetService.reset_password(email, new_password)
    return jsonify({'message': 'Password has been reset'}), 200