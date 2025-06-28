from flask import Flask
from skills import skills_bp  # Adjust the import path as needed

app = Flask(__name__)

app.register_blueprint(skills_bp, url_prefix='/api/skills')