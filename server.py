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

    # Check if user exists
    if username == "" or password == "":
        flash("Please enter both username and password")

    elif user:
        # Check if password is same as what is stored in database  
        if password == user.password:
            # Store user id and username in session when logged in
            session['user_id'] = user.user_id
            session['username'] = user.username
            
            # Redirect to diary page upon logging user in 
            return jsonify({"url": f'/diary/{user.username}'})
            
            # return redirect(f'/diary/{user.username}')
        else:
            #If pasword is incorrect flash notification
            flash("Password is incorrect. Please try again.")
    else:
        # If account does not exist promp user to create an account
        flash("This account doesn't exist, please create an account.")
    

    return redirect('/')

@app.route('/diary/<username>')
def visit_profile(username):
    """Visit a user's profile"""
    
    read_write = username == session['username']
    user_id = None
    # if not read_write:
    #     user_id = None

    print(session['username'])
    print(username)
    print(read_write)

    if read_write:

        #Get user id and username from session
        user_id = session['user_id']
       
    else: 
        # get user by username
        user = crud.get_user_by_username(username)
    
        print("$"*20)
        print(username)
        print(user)
        if user != None:
        # get user id
            user_id = user.user_id
        else: 
            username = session['username']
            return redirect(f'/diary/{username}')
        
    posts = crud.get_posts_by_user_id(user_id)
    
    return render_template('diary.html', posts = posts, username=username, read_write=read_write)

# route to log user out
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
    spotify_username = request.form.get('spotify_username')
    token = request.form.get('token')
    
    # query database to see if user exists
    user = crud.get_user_by_username(username)
    
    if username == "" or password == "" or spotify_username == "" or token == "":
        flash("Please complete all fields below.")

    # if user exists flash message
    elif user:
        flash("This account already exists")
    
    #if user does not already exist, create a new user 
    else:
        user = crud.create_user(username, password, spotify_username, token)
        flash("Account created, please log in")
        return redirect('/')

    return redirect('/create_account')

# Route to grab searched song from AJAX request in diary.js
# then content is queried into Spotify API to retrieve list
# of song results from search
@app.route('/diary_api.json', methods=['POST'])
def get_api_search():
    """Grab search data from form via AJAX post request in diary.js.
        Request is sending key value pair of {name: "searched song input from form"} 
        to the server then render search results from Spotify API as json data"""
   
    # Get form search content from 'name' key
    music_search = request.form.get('name')
    print("-------------------------")
    print("-------------------------")
    print(request.form.get('name'))
    print(music_search)
    # save results from Spotipy song search query as variable
    results = sp.search(music_search, limit = 5)

    # return json data that is ready to be handled on the frontend
    return jsonify(results["tracks"]["items"])

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
    post_content = request.form.get('post_content')
    date = datetime.now()

    post = crud.create_post(session['user_id'], date, post_content, spotify_id, music_title, music_img, music_url)
    
    username = session['username']

    return redirect(f'/diary/{username}')

# Delete song from database
@app.route('/delete_post', methods=['POST'])
def delete_post():
    """Grab song id from button"""

    post_id = request.form.get('post_id')
   
    post = crud.delete_user_post(session['user_id'], post_id)
     
    username = session['username']

    return redirect(f'/diary/{username}')

@app.route('/search', methods=["POST"])
def search_and_view_other_profiles():
    """Grab searched username and redirect to that user's profile
        page"""
    
    profile_search = request.form.get('search')
    user = crud.get_user_by_username(profile_search)

    return redirect(f'/diary/{user.username}')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
