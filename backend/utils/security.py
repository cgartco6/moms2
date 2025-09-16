# utils/security.py
import hashlib

def authenticate_user(username, password):
    # In a real application, this would check against a database
    # For demo purposes, we're using hardcoded values
    if username == "kelnic6" and password == "kelnic6s@6":
        return True
    return False

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not authenticate_user(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated
