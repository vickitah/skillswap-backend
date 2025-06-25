from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Skill(db.Model):
    tablename = 'skills'

id = db.Column(db.Integer, primary_key=True)
offering = db.Column(db.String(100), nullable=False)
wanting = db.Column(db.String(100), nullable=False)
description = db.Column(db.Text)
category = db.Column(db.String(100))
tags = db.Column(db.ARRAY(db.String))  
created_at = db.Column(db.DateTime, server_default=db.func.now())
user_email = db.Column(db.String(120))
rating = db.Column(db.Integer, default=0)
