from flask import Blueprint, request, jsonify, g
from models import Skill, db
from utils.auth import token_required

# ✅ Proper blueprint setup
skills_bp = Blueprint('skills', __name__)

# 📥 GET /api/skills — searchable, filterable feed
@skills_bp.route('/', methods=['GET'])
def get_skills():
    query = Skill.query

    search = request.args.get('search', '')
    category = request.args.get('category', '')
    tags = request.args.getlist('tags')  # e.g. ?tags=React&tags=Design

    if search:
        query = query.filter(
            (Skill.offering.ilike(f"%{search}%")) |
            (Skill.wanting.ilike(f"%{search}%")) |
            (Skill.description.ilike(f"%{search}%"))
        )

    if category:
        query = query.filter_by(category=category)

    if tags:
        for tag in tags:
            query = query.filter(Skill.tags.any(tag))

    skills = query.order_by(Skill.created_at.desc()).all()

    return jsonify([
        {
            'id': s.id,
            'offering': s.offering,
            'wanting': s.wanting,
            'description': s.description,
            'tags': s.tags,
            'category': s.category,
            'rating': s.rating,
            'created_at': s.created_at.isoformat(),
            'owner_email': s.user_email,
        } for s in skills
    ]), 200

# 📝 POST /api/skills — create a new exchange (requires auth)
@skills_bp.route('/', methods=['POST', 'OPTIONS'])  # ✅ Allow OPTIONS for CORS
@token_required
def create_skill():
    if request.method == 'OPTIONS':
        # ✅ CORS preflight response
        return '', 200

    data = request.get_json()
    user_email = g.user.email

    # 🪵 Debug logging
    print("📥 Incoming skill post:", data)
    print("🔐 Authenticated user:", user_email)

    try:
        new_skill = Skill(
            offering=data.get('offering'),
            wanting=data.get('wanting'),
            description=data.get('description'),
            tags=data.get('tags', []),
            category=data.get('category'),
            rating=0,
            user_email=user_email
        )

        db.session.add(new_skill)
        db.session.commit()

        print(f"✅ New skill created with ID {new_skill.id}")

        return jsonify({
            'message': 'Skill posted successfully!',
            'id': new_skill.id
        }), 201

    except Exception as e:
        print("❌ Error creating skill:", e)
        return jsonify({'error': 'Failed to create skill'}), 500
