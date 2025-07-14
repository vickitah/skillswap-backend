from flask import Flask, request, jsonify, g
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix
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
from flask_swagger_ui import get_swaggerui_blueprint

# ✅ Load .env variables
load_dotenv()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# ✅ App Config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv("SECRET_KEY")

# ✅ Init Extensions
db.init_app(app)
migrate = Migrate(app, db)

# ✅ CORS Setup
ALLOWED_ORIGINS = [
    "https://skillswap-frontend-henna.vercel.app",
    "http://localhost:5173"
]

CORS(app,
     supports_credentials=True,
     origins=ALLOWED_ORIGINS,
     allow_headers=["Content-Type", "Authorization"],
     expose_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

# ✅ Apply CORS to blueprints
for bp in [skills_bp, messages_bp, profile_bp, schedule_bp]:
    CORS(bp,
         supports_credentials=True,
         origins=ALLOWED_ORIGINS,
         allow_headers=["Content-Type", "Authorization"],
         expose_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

# ✅ Preflight allow for HTTPS enforcement
@app.before_request
def enforce_https_in_production():
    if request.method == "OPTIONS":
        return '', 200
    if not request.is_secure and os.getenv("FLASK_ENV") == "production":
        return jsonify({"message": "Use HTTPS"}), 400

# ✅ Firebase Admin Initialization
firebase_cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if firebase_cred_path and os.path.exists(firebase_cred_path):
    cred = credentials.Certificate(firebase_cred_path)
    firebase_admin.initialize_app(cred)
    print("✅ Firebase Admin initialized from file.")
else:
    firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
    if firebase_cred_json:
        try:
            firebase_cred_dict = json.loads(firebase_cred_json)
            cred = credentials.Certificate(firebase_cred_dict)
            firebase_admin.initialize_app(cred)
            print("✅ Firebase Admin initialized from JSON.")
        except ValueError as e:
            print("❌ Firebase JSON Error:", e)
            raise Exception("Firebase credentials are invalid.")
    else:
        print("❌ Firebase credentials missing.")
        raise Exception("Firebase credentials not found.")

# 🔐 Login Route
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    id_token = data.get("idToken")
    if not id_token:
        return jsonify({"message": "Missing idToken"}), 400

    try:
        decoded = firebase_auth.verify_id_token(id_token)
        uid = decoded["uid"]
        email = decoded.get("email")
        name = decoded.get("name") or email.split("@")[0]

        if not email:
            return jsonify({"message": "Invalid Firebase token"}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email, name=name)
            db.session.add(user)
            db.session.commit()

        payload = {
            "uid": uid,
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }

        token = jwt.encode(payload, app.secret_key, algorithm="HS256")
        return jsonify({"token": token, "name": user.name, "email": user.email}), 200

    except Exception as e:
        print("❌ Firebase verification failed:", e)
        return jsonify({"message": "Invalid ID token"}), 401

# 🔐 Protected Route
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

# ✅ CORS Test Route
@app.route("/api/cors-test", methods=["GET", "OPTIONS"])
def cors_test():
    return jsonify({"message": "CORS is working ✅"}), 200

# 📄 Swagger Docs
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "SkillSwap API Docs"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# 🌍 Root
@app.route('/')
def home():
    return "Welcome to SkillSwap API! 🚀"

# 🔁 Register Routes
app.register_blueprint(skills_bp, url_prefix='/api/skills')
app.register_blueprint(messages_bp, url_prefix='/api/messages')
app.register_blueprint(profile_bp, url_prefix='/api/profile')
app.register_blueprint(schedule_bp, url_prefix='/api/sessions')

# 🚀 Start Server
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
