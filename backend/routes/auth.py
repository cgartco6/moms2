# routes/auth.py
from flask import Blueprint, request, jsonify
from utils.security import authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if authenticate_user(username, password):
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401
