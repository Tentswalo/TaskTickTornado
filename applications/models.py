from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority = db.Column(db.String(20), nullable=False, default='Medium')
    status = db.Column(db.String(20), nullable=False, default='Pending')
    due_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
