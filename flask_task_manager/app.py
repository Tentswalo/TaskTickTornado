from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use an SQLite in-memory database for testing purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def home():
    return "Flask and SQLAlchemy are working!"

if __name__ == '__main__':
    app.run(debug=True)
