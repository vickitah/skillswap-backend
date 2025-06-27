
from flask import Blueprint, request, jsonify
from models import db, User
from utils.auth import token_required

profile_bp = Blueprint("profile", __name__)

# Get Profile
@profile_bp.route("/<username>", methods=["GET"])
def get_profile(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "name": user.name,
        "email": user.email,
        "tagline": user.tagline or "",
        "skills_offered": [
            {"name": s.name, "level": s.level, "exchanges_completed": s.exchanges_completed}
            for s in user.skills_offered
        ],
        "skills_wanted": [
            {"name": s.name, "priority": s.priority}
            for s in user.skills_wanted
        ],
        "exchanges": [
            {"partner_name": ex.partner_name, "teaching": ex.teaching, "learning": ex.learning, "status": ex.status}
            for ex in user.exchanges
        ]
    })

# Update Profile (JWT)
@profile_bp.route("/update", methods=["PUT"])
@token_required
def update_profile():
    user_email = request.user["email"]
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    user.name = data.get("name", user.name)
    user.tagline = data.get("tagline", user.tagline)

    try:
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update profile", "error": str(e)}), 500