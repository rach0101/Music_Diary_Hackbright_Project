"""Models for Music Diary Project"""

# First step is to complete Model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app, echo=True):
    """Connect to diary database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///diary"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

    print("Connected to the db!")

app = Flask(__name__)

connect_to_db(app)

class User(db.Model):
    """Create instance of table"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement=True,)

    username = db.Column(db.String(50), 
                      nullable=False, 
                      unique = True,)

    password = db.Column(db.String(50),
                         nullable=False, 
                         unique = False,)

    spotify_username = db.Column(db.String(50), 
                      nullable=False, 
                      unique = True,)                     

    token = db.Column(db.String(), 
                      nullable=False, 
                      unique = True,)                       

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"