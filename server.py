"""Server for Music Diary App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud 
from jinja2 import StrictUndefined
import spotipy, requests, os
from spotipy.oauth2 import SpotifyClientCredentials
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
    # at some point I will want to get name from session and display greeting
    
    return render_template('diary.html')


@app.route('/diary_api.json', methods=['POST'])
def get_api_search():
    """Grab data from search form and render from api as json"""
   
    # grab search data from form
    music_search = request.form.get('name')
    print("******************")
    print(music_search)
    results = sp.search(music_search, limit = 5)
    for item in results["tracks"]["items"]:
        song_name = item['name']
        album_art =item['album']['images'][2]['url']

        # get song name
        print(item['name'])
        
        # get link to song
        print(item['external_urls'])
        
        print("******************")
        # get artist names
        for artist in item['artists']:
            print(artist['name'])
        
        print("******************")
        # # get album name
        print(item['album']['name']) 
        
        print("******************")
        # get large album art
        print(item['album']['images'][0]['url'])

        print("******************")
        # get small album art
        print(item['album']['images'][2]['url'])
        
        print("***____________________*****") 
        print(jsonify(results["tracks"]["items"]))
        print(results)
        
        # jsonify(results["tracks"]["items"][0])
    return jsonify(results["tracks"]["items"])


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
