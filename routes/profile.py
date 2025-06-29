from flask import Blueprint, request, jsonify, g
from models import db, User, SkillOffered, SkillWanted
from utils.auth import token_required

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/update", methods=["PUT"])
@token_required
def update_profile():
    user_email = g.user.email
    user = User.query.filter_by(email=user_email).first()
    data = request.get_json()

    if not user:
        # Create new user
        user = User(
            email=user_email,
            name=data.get("name"),
            tagline=data.get("tagline", ""),
        )
        db.session.add(user)
        db.session.commit()

    # Update basic info
    user.name = data.get("name", user.name)
    user.tagline = data.get("tagline", user.tagline)

    # 🛠️ Optional: Update offered skills
    if "skills_offered" in data:
        user.skills_offered.clear()  # Clear old list
        for s in data["skills_offered"]:
            skill = SkillOffered(
                name=s["name"],
                level=s.get("level", "Beginner"),
                exchanges_completed=s.get("exchanges_completed", 0),
                user=user
            )
            db.session.add(skill)

    # 🛠️ Optional: Update wanted skills
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
