from flask_sqlalchemy import SQLAlchemy
from app import *
db = SQLAlchemy()


class User(db.Model):
    """User_model"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(100),  nullable=False)
#    hashed_pswd = db.Column(db.String(), nullable=False)

