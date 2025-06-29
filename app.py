from flask import Flask, request, jsonify, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import jwt
import datetime
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
import json

from models import db, User
from routes.skills import skills_bp
from routes.profile import profile_bp
from routes.messages import messages_bp
from routes.session import schedule_bp
from utils.auth import token_required

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")

CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# ✅ Firebase Admin SDK initialization (using environment variable)
firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS_JSON")

if firebase_cred_json:
    try:
        # Load Firebase credentials from the environment variable
        cred = credentials.Certificate(json.loads(firebase_cred_json))
        firebase_admin.initialize_app(cred)
    except ValueError as e:
        print("Error loading Firebase credentials from environment:", e)
        raise Exception("Firebase credentials are invalid.")
else:
    print("Firebase credentials not found. Please set FIREBASE_CREDENTIALS_JSON environment variable.")

# 🔐 Firebase Login + JWT Issuance
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    id_token = data.get("idToken")

    if not id_token:
        return jsonify({"message": "Missing idToken"}), 400

    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        email = decoded_token.get("email")

        if not email:
            return jsonify({"message": "Invalid Firebase token"}), 400

        # Create or find user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email, name=email.split("@")[0])
            db.session.add(user)
            db.session.commit()

        payload = {
            "uid": uid,
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }

        token = jwt.encode(payload, app.secret_key, algorithm="HS256")
        return jsonify({"token": token}), 200

    except Exception as e:
        print("Firebase verification error:", e)
        return jsonify({"message": "Invalid ID token"}), 401

# 🔐 Test protected route
@app.route("/api/protected", methods=["GET"])
@token_required
def protected():
    return jsonify({
        "message": f"Welcome {g.user.email}, you're authenticated!",
        "user": {
            "id": g.user.id,
            "email": g.user.email,
            "name": g.user.name
        }
    }), 200

# 🔗 Register Blueprints (each already prefixed with `/api`)
app.register_blueprint(skills_bp, url_prefix='/api/skills')
app.register_blueprint(messages_bp, url_prefix='/api/messages')
app.register_blueprint(profile_bp, url_prefix='/api/profile')
app.register_blueprint(schedule_bp, url_prefix='/api/sessions')  # For scheduling

# 🚀 Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
