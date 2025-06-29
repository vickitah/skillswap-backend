from flask import request, jsonify, current_app, g
from functools import wraps
import jwt
from models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method == 'OPTIONS':
            return f(*args, **kwargs)  # Allow CORS preflight

        token = None
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Missing token"}), 401

        try:
            data = jwt.decode(token, current_app.secret_key, algorithms=["HS256"])
            user = User.query.filter_by(email=data["email"]).first()
            if not user:
                return jsonify({"message": "User not found"}), 404
            g.user = user  # ✅ assign full User model object
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)
    return decorated
