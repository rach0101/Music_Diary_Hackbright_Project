"""Models for Music Diary Project"""

# First step is to complete Model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///diary", echo=True):
    """Connect to diary database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


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

    if __name__ == '__main__':
        from server import app
        connect_to_db(app)