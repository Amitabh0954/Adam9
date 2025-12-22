from flask import Blueprint, request, jsonify
from backend.services.auth.login_service import LoginService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    try:
        session_id = LoginService.login(username, password)
        return jsonify({"message": "Login successful", "session_id": session_id}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400