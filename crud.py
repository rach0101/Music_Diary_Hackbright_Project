from model import db, User, Post, connect_to_db

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import desc

# Create Users table
def create_user(username, password, spotify_username, token):
    
    user = User(username=username, password=password, 
                spotify_username=spotify_username, token=token)

    db.session.add(user)
    db.session.commit()

    return user

# Create Posts Table
def create_post(user_id, date, post_content, spotify_id, music_title, 
                music_img, music_url):
    
    post = Post(user_id=user_id, date=date, post_content=post_content, 
                spotify_id=spotify_id, music_title=music_title, music_type="song", 
                music_img=music_img, music_url=music_url)


    db.session.add(post)
    db.session.commit()

    return post

# Queries for users and accounts
def get_users():
    """Return a list of user records"""
    
    return User.query.get(user_id)

def get_user_by_username(username):
    """Return a user object by username"""

    user = User.query.filter(User.username == username).first()

    return user

def get_posts_by_user_id(user_id):
    """Return all posts with the given user id"""
   
    # correct this line of code so that it works correctly
    posts = Post.query.filter(Post.user_id == user_id)

    return posts.order_by(desc(Post.post_id)).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)