from flask import Blueprint, request, jsonify, g
from models import db, User, SkillOffered, SkillWanted
from utils.auth import token_required

profile_bp = Blueprint("profile", __name__)

# ✅ GET /api/profile/<username> — fetch user profile
@profile_bp.route("/<username>", methods=["GET"])
def get_profile(username):
    user = User.query.filter_by(name=username).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    profile_data = {
        "name": user.name,
        "email": user.email,
        "tagline": user.tagline,
        "rating": user.rating,
        "reviews": user.reviews,
        "total_exchanges": user.total_exchanges,
        "skills_offered": [
            {
                "name": s.name,
                "level": s.level,
                "exchanges_completed": s.exchanges_completed
            } for s in user.skills_offered
        ],
        "skills_wanted": [
            {
                "name": s.name,
                "priority": s.priority
            } for s in user.skills_wanted
        ],
        "exchanges": [],  # You can populate this later
        "username": user.name  # Used in frontend comparison
    }

    return jsonify(profile_data), 200

# ✅ PUT /api/profile/update — update or create profile
@profile_bp.route("/update", methods=["PUT"])
@token_required
def update_profile():
    user_email = g.user.email
    user = User.query.filter_by(email=user_email).first()
    data = request.get_json()

    if not user:
        user = User(
            email=user_email,
            name=data.get("name"),
            tagline=data.get("tagline", "")
        )
        db.session.add(user)
        db.session.commit()

    user.name = data.get("name", user.name)
    user.tagline = data.get("tagline", user.tagline)

    # 🧹 Clear old skills and add new ones
    if "skills_offered" in data:
        user.skills_offered.clear()
        for s in data["skills_offered"]:
            skill = SkillOffered(
                name=s["name"],
                level=s.get("level", "Beginner"),
                exchanges_completed=s.get("exchanges_completed", 0),
                user=user
            )
            db.session.add(skill)

    if "skills_wanted" in data:
        user.skills_wanted.clear()
        for s in data["skills_wanted"]:
            skill = SkillWanted(
                name=s["name"],
                priority=s.get("priority", False),
                user=user
            )
            db.session.add(skill)

    try:
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update profile", "error": str(e)}), 500
