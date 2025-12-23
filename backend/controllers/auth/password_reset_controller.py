from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/request_reset', methods=['POST'])
def request_reset():
    data = request.json
    email = data.get('email')
    
    password_reset = PasswordResetService.request_password_reset(email)
    # Send email logic should be here
    return jsonify({'message': 'Password reset link sent to email'})


@reset_bp.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('new_password')
    
    success = PasswordResetService.reset_password(token, new_password)
    if success:
        return jsonify({'message': 'Password has been reset successfully'})
    return jsonify({'error': 'Invalid or expired token'}), 400