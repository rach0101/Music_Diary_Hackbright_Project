from model import db, User, Post, connect_to_db

# Create Users and Posts
def create_user(username, password, spotify_username, token):
    
    user = User(username=username, password=password, 
                spotify_username=spotify_username, token=token)

    db.session.add(user)
    db.session.commit()

    return user

def create_post(user_id, date, post_content, spotify_id, music_title, music_type):
    
    post = Post(user_id=user_id, date=date, post_content=post_content, 
                song_id=song_id, album_id=album_id, playlist_id=playlist_id)

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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)