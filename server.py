"""Server for Music Diary App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud 
from jinja2 import StrictUndefined
import spotipy, requests, os
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
# os.system("source secrets.sh")

app = Flask(__name__)
app.secret_key = "dev"
# app.secret_key = os.environ['APP_KEY']
app.jinja_env.undefined = StrictUndefined

# add Spotipy auth
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


@app.route('/')
def home():
    """View Homepage"""

    return render_template('home.html')

@app.route('/diary')
def diary():
    """View Diary"""
    
    return render_template('diary.html')


@app.route('/diary_api.json', methods=['POST'])
def get_api_search():
    """Grab data from search form and render from api as json"""
   
    # grab search data from form
    music_search = request.form.get('name')
    
    results = sp.search(music_search, limit = 5)
    for item in results["tracks"]["items"]:
        song_name = item['name']
        album_art =item['album']['images'][2]['url']

        # get song name
        print(item['name'])
        
        # get link to song
        print(item['external_urls'])
        
        # get artist names
        # for artist in item['artists']:
        #     print(artist['name'])
        
        # # # get album name
        # print(item['album']['name']) 
        
        # # get large album art
        # print(item['album']['images'][0]['url'])

        # # get small album art
        # print(item['album']['images'][2]['url'])
        # print("******************")

    return jsonify(results["tracks"]["items"])

# Create a route that grabs data form form and saves to database
@app.route('/save_song_to_database', methods=['POST'])
def save_post_to_database():
    """Grab selected item from search results and send to front end"""
    music_title = request.form.get('name')
    song_url = request.form.get('url')
    song_img = request.form.get('img')
    spotify_id = request.form.get('id')
    song_img = request.form.get('img')
    post_content = request.form.get('post_content')
    date = datetime.now()

    # print(song_name + " " + song_url + " " + post_content)
    # print(date)
    
    # Crete function in crud
    # grab user id from session
    # how do i grab the date??
    # setting music type to song
    # make sure to add img and url to database

    post = crud.create_post(session['user_id'], date, post_content, spotify_id, music_title)
    flash("new post just created!")
    
    return render_template('diary.html')

@app.route('/login', methods=["POST"])
def login_user():
    """Retrieve username and password from login page"""
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = crud.get_user_by_username(username)

    if user:
        
        if password == user.password:
            #flash to user that they logged in
            session['user_id'] = user.user_id
            # session['username'] = user.username
            flash("Logged in successfully")
            return redirect('/diary')
        else:
            #If pasword is incorrect flash notification
            flash("Password is incorrect!")
    else:
        flash("This account doesn't exist, please create an account")

    return redirect('/')

@app.route('/create_account')
def create_account():
    """Create a New Account and Display Form"""
  
    return render_template('create_account.html')

@app.route('/create_new_account', methods=["POST"])
def create_new_account():
    """When Form is Submitted Create a New Account"""
    username = request.form.get('username')
    password = request.form.get('password')
    spotify_username = request.form.get('spotify_username')
    token = request.form.get('token')
    # query database to see if use exists
    user = crud.get_user_by_username(username)

    if user:
        flash("This account already exists")
        
    else:
        user = crud.create_user(username, password, spotify_username, token)
        flash("Account created, please log in")

    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
