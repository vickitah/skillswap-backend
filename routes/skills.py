from flask import Blueprint, request, jsonify
from models import Skill, db
try:
    from utils.auth import token_required
except ImportError:
    # Dummy decorator if auth is not available
    from flask import request
    def token_required(f):
        def decorated(*args, **kwargs):
            # Set a dummy user for testing if auth is not available
            request.user = {'email': 'dummy@example.com'}
            return f(*args, **kwargs)
        return decorated

skills_bp = Blueprint('skills', __name__)

# GET /api/skills - filterable feed
@skills_bp.route('', methods=['GET'])
def get_skills():
    query = Skill.query

    search = request.args.get('search', '')
    category = request.args.get('category', '')
    tags = request.args.getlist('tags')  # e.g. ?tags[]=React&tags[]=Design

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
            'owner_email': s.owner_email,
        } for s in skills
    ]), 200

# POST /api/skills - create a new skill exchange
@skills_bp.route('', methods=['POST'])
@token_required
def create_skill():
    data = request.get_json()
    user_email = request.user['email']  # get from JWT

    new_skill = Skill(
        offering=data.get('offering'),
        wanting=data.get('wanting'),
        description=data.get('description'),
        tags=data.get('tags', []),
        category=data.get('category'),
        rating=0,
        owner_email=user_email  # set owner
    )

    db.session.add(new_skill)
    db.session.commit()

    return jsonify({
        'message': 'Skill posted successfully!',
        'id': new_skill.id
    }), 201
