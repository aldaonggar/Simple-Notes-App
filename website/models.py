from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128)) #TODO hash passwords
    firstName = db.Column(db.String(128))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    note = db.Column(db.String(512))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.relationship('Note')