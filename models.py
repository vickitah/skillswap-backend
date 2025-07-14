from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Used for profile URL
    email = db.Column(db.String(120), unique=True, nullable=False)
    tagline = db.Column(db.String(255))

    # Relationships
    skills_offered = db.relationship('SkillOffered', backref='user', lazy=True)
    skills_wanted = db.relationship('SkillWanted', backref='user', lazy=True)
    exchanges = db.relationship('Exchange', backref='user', lazy=True)


class SkillOffered(db.Model):
    __tablename__ = 'skills_offered'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50))  # e.g., Beginner, Intermediate, Expert
    exchanges_completed = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class SkillWanted(db.Model):
    __tablename__ = 'skills_wanted'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(50))  # e.g., High, Medium, Low
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Exchange(db.Model):
    __tablename__ = 'exchanges'

    id = db.Column(db.Integer, primary_key=True)
    partner_name = db.Column(db.String(100))  # just storing name for now
    teaching = db.Column(db.String(100))
    learning = db.Column(db.String(100))
    next_session = db.Column(db.DateTime)
    status = db.Column(db.String(50), default='Scheduled')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Skill(db.Model):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    offering = db.Column(db.String(100), nullable=False)
    wanting = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    tags = db.Column(ARRAY(db.String))  # PostgreSQL-specific
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_email = db.Column(db.String(120))  # Not linked to User model (can be migrated later)
    rating = db.Column(db.Integer, default=0)



class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    sender_email = db.Column(db.String(120), nullable=False)
    receiver_email = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), default='message')  
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(500))
    status = db.Column(db.String(20), default="pending")
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
