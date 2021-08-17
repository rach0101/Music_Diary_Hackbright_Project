from model import db, User, Post, Song, Album, Playlist, connect_to_db

def create_user(username, password, spotify_username, token):
    user = User(username=username, password=password, spotify_username=spotify_username, token=token)

    db.session.add(user)
    db.session.commit()

    return user

def create_post(user_id, date, post_content, song_id, album_id, playlist_id):
    post = Post(user_id=user_id, date=date, post_content=post_content, song_id=song_id, album_id=album_id, playlist_id=playlist_id)

    db.session.add(post)
    db.session.commit()

    return post

def create_song(song_title):
    song = Song(song_title=song_title)

    db.session.add(song)
    db.session.commit()

    return song

def create_album(album_title):
    album = Album(album_title=album_title)

    db.session.add(album)
    db.session.commit()

    return album

def create_playlist(playlist_title):
    playlist = Playlist(playlist_title=playlist_title)

    db.session.add(playlist)
    db.session.commit()

    return playlist


if __name__ == '__main__':
    from server import app
    connect_to_db(app)