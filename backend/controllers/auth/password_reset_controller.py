from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService

password_reset_bp = Blueprint('password_reset', __name__)

@password_reset_bp.route('/request-reset', methods=['POST'])
def request_reset():
    data = request.get_json()
    email = data.get('email')
    try:
        token = PasswordResetService.generate_reset_token(email)
        # Here you would typically send an email to the user with the token
        return jsonify({"message": "Password reset link sent", "token": token}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@password_reset_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    try:
        PasswordResetService.reset_password(token, new_password)
        return jsonify({"message": "Password has been reset successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400