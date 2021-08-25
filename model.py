"""Models for Music Diary Project"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, echo=True):
    """Connect to diary database."""

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///diary"
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

# Create an instance of the user table
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

    # create relationship between users and posts

    post = db.relationship("Post", backref="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"

# Create an instance of the Post table
class Post(db.Model):
    """Create instance of table"""

    __tablename__ = 'posts'

    post_id= db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement=True,)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    date = db.Column(db.DateTime)

    post_content = db.Column(db.String(200), 
                      nullable=False, 
                      unique = True,)  

    spotify_id = db.Column(db.String())

    music_title = db.Column(db.String(75))

    music_type = db.Column(db.String(8))

    music_img = db.Column(db.String())

    music_url = db.Column(db.String())

    # user = a list of user objects

    def __repr__(self):
        return f"<Post post_id={self.post_id} post_content={self.post_content}>"


    if __name__ == '__main__':
        from server import app
        connect_to_db(app)