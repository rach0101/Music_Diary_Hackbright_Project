from model import db, User, Post, connect_to_db

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

if __name__ == '__main__':
    from server import app
    connect_to_db(app)