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

    if username:

        user = User.query.filter(User.username == username).first()
        return user

    else:
        return None
    

def get_posts_by_user_id(user_id):
    """Return all posts with the given user id"""
   
    posts = Post.query.filter(Post.user_id == user_id)
    print("-------crud.py user_id check 4-------")
    print(user_id)
    return posts.order_by(desc(Post.post_id)).all()


# function to get post by user_id and post_id and delete
def delete_user_post(user_id, post_id):
    """Return all posts with the given user id and post id
    then delete"""
   
    post = Post.query.filter(Post.user_id == user_id,
                                Post.post_id == post_id).first()
    db.session.delete(post)
    db.session.commit()

    return post

if __name__ == '__main__':
    from server import app
    connect_to_db(app)