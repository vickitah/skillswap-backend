from flask import Blueprint, request, jsonify
from models import Skill, db
from utils.auth import token_required

skills_bp = Blueprint('skills', __name__)

@skills_bp.route('', methods=['GET'])
def get_skills():
    query = Skill.query

    search = request.args.get('search', '')
    category = request.args.get('category', '')
    tags = request.args.getlist('tags')  

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
            'created_at': s.created_at.isoformat()
        } for s in skills
    ])

@skills_bp.route('', methods=['POST'])
def create_skill():
    data = request.get_json()

    new_skill = Skill(
        offering=data.get('offering'),
        wanting=data.get('wanting'),
        description=data.get('description'),
        tags=data.get('tags', []),
        category=data.get('category'),
        rating=0
    )

    db.session.add(new_skill)
    db.session.commit()

    return jsonify({
        'message': 'Skill posted successfully!',
        'id': new_skill.id
    }), 201