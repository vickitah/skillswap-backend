from flask import Blueprint, request, jsonify, g
from models import db, Session, User
from datetime import datetime
from utils.auth import token_required

schedule_bp = Blueprint('schedule', __name__)

# 📅 Schedule a session
@schedule_bp.route('/', methods=['POST', 'OPTIONS'])
@token_required
def schedule_session():
    if request.method == 'OPTIONS':
        return '', 200  # ✅ CORS preflight

    data = request.get_json()
    requester_id = g.user.id
    recipient_email = data.get('recipient_email')
    time_str = data.get('scheduled_time')
    message = data.get('message', '')

    if not recipient_email or not time_str:
        return jsonify({"error": "Missing recipient email or time"}), 400

    recipient = User.query.filter_by(email=recipient_email).first()
    if not recipient:
        return jsonify({"error": "Recipient not found"}), 404

    try:
        scheduled_time = datetime.fromisoformat(time_str)
    except ValueError:
        return jsonify({"error": "Invalid datetime format"}), 400

    new_session = Session(
        requester_id=requester_id,
        recipient_id=recipient.id,
        scheduled_time=scheduled_time,
        message=message
    )

    db.session.add(new_session)
    db.session.commit()

    return jsonify({"message": "Session scheduled successfully"}), 201


# 📄 Fetch all sessions for the logged-in user
@schedule_bp.route('/', methods=['GET', 'OPTIONS'])
@token_required
def get_sessions():
    if request.method == 'OPTIONS':
        return '', 200  # ✅ CORS preflight

    user_id = g.user.id

    sessions = Session.query.filter(
        (Session.requester_id == user_id) | (Session.recipient_id == user_id)
    ).order_by(Session.scheduled_time.desc()).all()

    result = []
    for s in sessions:
        result.append({
            "id": s.id,
            "requester_id": s.requester_id,
            "recipient_id": s.recipient_id,
            "scheduled_time": s.scheduled_time.isoformat(),
            "message": s.message,
            "status": s.status
        })

    return jsonify(result), 200


# ✅ PATCH: Update session status
@schedule_bp.route('/<int:session_id>/', methods=['PATCH', 'OPTIONS'])
@token_required
def update_session_status(session_id):
    if request.method == 'OPTIONS':
        return '', 200  # ✅ Preflight CORS

    session = Session.query.get(session_id)
    if not session:
        return jsonify({'error': 'Session not found'}), 404

    data = request.get_json()
    new_status = data.get('status')

    if new_status not in ['pending', 'accepted', 'rejected']:
        return jsonify({'error': 'Invalid status value'}), 400

    session.status = new_status
    db.session.commit()

    return jsonify({'message': f'Session {session_id} updated to {new_status}'}), 200
