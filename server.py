"""Server for Music Diary App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud 
from jinja2 import StrictUndefined
import spotipy, requests, os
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import random 
# os.system("source secrets.sh")

app = Flask(__name__)
app.secret_key = "dev"
# app.secret_key = os.environ['APP_KEY']
app.jinja_env.undefined = StrictUndefined

#Spotipy Auth
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# Route to render template of homepage
@app.route('/')
def home():
    """View Homepage"""

    return render_template('home.html')

# Route to diary homepage where user can log in
# or create an account
@app.route('/login', methods=["POST"])
def login_user():
    """Retrieve username and password from login page
        if user already exists log user in, otherwise
        prompt user to create a new account"""

    # Grab username and password from home.html forms 
    username = request.form.get('username')
    password = request.form.get('password')

    # Get user object from database 
    user = crud.get_user_by_username(username)
   
    if not user:
        if username and not user:
            flash("User does not exist. Please create a new account.")
        elif not username or not password:
            flash("Please enter both a username and password")

        return jsonify({"url": '/'})
    else:
        # Check if password is same as what is stored in database  
        if password == user.password:
            # Store user id and username in session when logged in
            session['user_id'] = user.user_id
            session['username'] = user.username
            # Redirect to diary page upon logging user in 
            return jsonify({"url": f'/diary/{user.username}'})

        else:
            flash("Please enter a valid password")
            return jsonify({"url": '/'})
    

@app.route('/diary/<username>')
def visit_profile(username):
    """Visit a user's profile"""
    
    read_write = username == session['username']
    user_id = None

    if read_write:
        #Get user id and username from session
        user_id = session['user_id']
       
    else: 
        # get user by username
        user = crud.get_user_by_username(username)

        if user != None:
        # get user id
            user_id = user.user_id
        else: 
            username = session['username']
            return redirect(f'/diary/{username}')
    
    posts = crud.get_posts_by_user_id(user_id)
    
    return render_template('diary.html', posts = posts, username=username, read_write=read_write)

# Route to log user out
@app.route('/logout')
def logout_user():
    """Log user out"""
    
    session.clear()

    return redirect('/')

# Route to render create account template
@app.route('/create_account')
def create_account():
    """Create a New Account and Display Form"""
  
    return render_template('create_account.html')

# Route that grabs new account data from form and
# saves to the Users database as a new user
@app.route('/create_new_account', methods=["POST"])
def create_new_account():
    """When Form is Submitted Create a New Account"""

    # Grab username, password, spotify_username and token 
    # from create_account.html forms
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Generate random Spotify usernames and tokens
    spotify_username = random.randint(100000, 999999999999999999999999)
    token = random.randint(100000, 999999999999999999999999)

    # query database to see if user exists
    user = crud.get_user_by_username(username)
    
    if username == "" or password == "":
        flash("Please complete all fields below.")
    
    # if user exists flash message
    elif user:
        flash("This account already exists")
    
    #if user does not already exist, create a new user 
    else:
        user = crud.create_user(username, password, str(spotify_username), str(token))
        flash("Account created, please log in")
        return redirect('/')

    return redirect('/create_account')

# Route to grab searched song from AJAX request in diary.js
# then content is queried into Spotify API to retrieve list
# of song results from search.
@app.route('/diary_api.json', methods=['POST'])
def get_api_search():
    """Grab search data from form via AJAX post request in diary.js.
        Request is sending key value pair of {name: "searched song input from form"} 
        to the server then render search results from Spotify API as json data"""
   
    # Get form search content from 'name' key
    music_search = request.form.get('name')
   
    # save results from Spotipy song search query as variable
    results = sp.search(music_search, limit = 5, type="track,album")
    
    # Return a json dictionary of album and track data. There will 
    # be 5 albums and 5 tracks in the response object
    return jsonify(results)
   

# Create a route that grabs data form the create post form (form in the #music_comment div in diary.html)
# and saves song data to database using crud.py
# song data will be stored in hidden form inputs which have placeholder values that are updated in
# diary.js. Then server uses get request to grab values from the input fields with the specified IDs.  
@app.route('/save_song_to_database', methods=['POST'])
def save_post_to_database():
    """Grab selected item from search results and send to front end"""
    music_title = request.form.get('name')
    music_url = request.form.get('url')
    music_img = request.form.get('img')
    spotify_id = request.form.get('id')
    music_type = request.form.get('type')
    artist_name = request.form.get('artist')
    artist_url = request.form.get('artist_url')
    post_content = request.form.get('post_content')
    date = datetime.now()
    
    print(music_type)
    print(artist_name)
    print(artist_url)

    username = session['username']

    if post_content == "":
        flash("please enter post content.")
        print("don't save this")

    else:
        post = crud.create_post(session['user_id'], date, post_content, spotify_id, music_title, music_type, music_img, music_url, artist_name, artist_url)
    
    return redirect(f'/diary/{username}')

# Delete song from database
@app.route('/delete_post', methods=['POST'])
def delete_post():
    """Grab song id from button"""

    post_id = request.form.get('post_id')

    # Use user_id from session and post_id from ajax post request
    # in diary.js to delete post on form submit (delete button click).
    post = crud.delete_user_post(session['user_id'], post_id)
    
    # Get username from session 
    username = session['username']
    
    # Load all posts by user in session so that 
    # selected post can be deleted from the HTML
    posts = crud.get_posts_by_user_id(session['user_id'])

    # Send post_id to the front end so that the HTML 
    # element can be removed.
    return post_id
    

@app.route('/search', methods=["POST"])
def search_and_view_other_profiles():
    """Grab searched username and redirect to that user's profile
        page"""
    
    # Get searched username from form on frontend
    profile_search = request.form.get('search')

    # Query user table to get user from username search
    user = crud.get_user_by_username(profile_search)
    # Check if user exists
    if user != None:
        return redirect(f'/diary/{user.username}')
    else: 
        flash("Please enter a valid username.")
        username = session['username']
        return redirect(f'/diary/{username}')

@app.route('/like_post', methods=["POST"])
def add_like_to_post():
    """Get like on click and add to 
    user's posts"""

    # Get username from session
    username = session['username']
    # Get user id from session
    user_id = session['user_id']

    # Get post id from ajax post request
    post_id = request.form.get('post_id') 

    # Create a like in the database using
    # the user id and post id.
    like = crud.create_like(user_id, post_id)
    
    # Get list of all like objects in database 
    # for the given post id. Count the length of 
    # the list (total number of likes) and send to frontend
    # as a dictionary.
    like_count = crud.get_likes_by_post_id(post_id)

    return jsonify({"like_count": len(like_count),
                     "post_id": post_id})

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
