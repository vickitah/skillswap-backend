from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

db = SQLAlchemy()

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
