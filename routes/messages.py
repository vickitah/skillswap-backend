from flask import Blueprint, request, jsonify, g
from models import db, Message
from utils.auth import token_required

messages_bp = Blueprint("messages", __name__)

@messages_bp.route('/', methods=['POST', 'OPTIONS'])
@token_required
def send_message():
    if request.method == 'OPTIONS':
        return '', 200  # ✅ Allow preflight CORS

    data = request.get_json()
    sender_email = g.user.email
    receiver_email = data.get("receiver_email")
    content = data.get("content")

    if not receiver_email or not content:
        return jsonify({"error": "Missing fields"}), 400

    new_message = Message(
        sender_email=sender_email,
        receiver_email=receiver_email,
        content=content
    )
    db.session.add(new_message)
    db.session.commit()
    
    return jsonify({"message": "Message sent"}), 201


@messages_bp.route('/', methods=['GET', 'OPTIONS'])
@token_required
def get_messages():
    if request.method == 'OPTIONS':
        return '', 200  # ✅ Allow preflight CORS

    user_email = g.user.email
    messages = Message.query.filter(
        (Message.sender_email == user_email) | (Message.receiver_email == user_email)
    ).order_by(Message.timestamp.desc()).all()

    return jsonify([
        {
            "id": m.id,
            "sender": m.sender_email,
            "receiver": m.receiver_email,
            "content": m.content,
            "timestamp": m.timestamp.isoformat()
        } for m in messages
    ]), 200
