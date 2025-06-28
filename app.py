from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import jwt
import datetime
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from flask_migrate import Migrate

from models import db
from routes.skills import skills_bp
from utils.auth import token_required

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Firebase
cred = credentials.Certificate("firebase_admin.json")
firebase_admin.initialize_app(cred)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    id_token = data.get("idToken")
    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token["uid"]
        email = decoded_token.get("email", "")
        payload = {
            "uid": uid,
            "email": email,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
        }
        token = jwt.encode(payload, app.secret_key, algorithm="HS256")
        return jsonify({"token": token}), 200
    except Exception as e:
        print("Error verifying Firebase ID token:", e)
        return jsonify({"message": "Invalid ID token"}), 401

@app.route("/protected", methods=["GET"])
@token_required
def protected():
    user = request.user
    return jsonify({
        "message": f"Welcome {user['email']}, you're authenticated!",
        "user": user
    }), 200

# Register routes
app.register_blueprint(skills_bp, url_prefix='/api/skills')

if __name__ == "__main__":
    app.run(debug=True)
