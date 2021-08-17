"""Server for Music Diary App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
    """View Homepage"""

    return render_template('home.html')

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
            flash("Logged in successfully")
            return render_template('diary.html')
        else:
            #If pasword is incorrect flash notification
            flash("Password is incorrect!")
    else:
        flash("This account doesn't exist, please create an account")

    return redirect('/')

@app.route('/create_account')
def create_account():
    """Create a New Account"""

    return render_template('create_account.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
