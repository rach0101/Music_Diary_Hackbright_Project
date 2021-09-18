from model import db, User, Post, Like, connect_to_db

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import desc, and_

# Create Users table
def create_user(username, password):
    """Create a user"""

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user


# Create Posts Table
def create_post(user_id, date, post_content, spotify_id, music_title, 
                music_type, music_img, music_url, artist_name, artist_url):
    """Create a post"""

    post = Post(user_id=user_id, date=date, post_content=post_content, 
                spotify_id=spotify_id, music_title=music_title, music_type=music_type, 
                music_img=music_img, music_url=music_url, artist_name=artist_name, artist_url=artist_url)
    db.session.add(post)
    db.session.commit()
    return post


# Queries for users and accounts
def get_users():
    """Return a list of user records"""
    
    return User.query.get(user_id)


def get_user_by_username(username):
    """Return a user object by username."""
    
    user = User.query.filter(User.username == username).first()
    return user


def get_posts_by_user_id(user_id):
    """Return all posts with the given user id"""
   
    # Query posts table to get posts by user id  and joins loaded query data with likes table
    # so that the related rows (likes in this case) are loaded in the same results set.
    posts = Post.query.filter(Post.user_id == user_id).options(db.joinedload("likes"))
    return posts.order_by(desc(Post.post_id)).all()


# Function to get post by user_id and post_id and delete
def delete_user_post(user_id, post_id):
    """Return all posts with the given user id and post id
    then delete"""
   
    post = Post.query.filter(Post.user_id == user_id, Post.post_id == post_id).first()
    db.session.delete(post)
    db.session.commit()
    return post


def create_like(poster_user_id, post_id):
    """Create a like"""

    existing_likes = Like.query.filter(and_(Like.post_id == post_id, Like.poster_user_id == poster_user_id)).all()
    
    if not existing_likes:
        like = Like(poster_user_id = poster_user_id, post_id = post_id)
        db.session.add(like)
        db.session.commit()
        return like
    else:
        return None


def get_likes_by_post_id(post_id):
    """Return all likes with the given post id"""
   
    likes = Like.query.filter(Like.post_id == post_id).all()
    return likes

if __name__ == '__main__':
    from server import app
    connect_to_db(app)