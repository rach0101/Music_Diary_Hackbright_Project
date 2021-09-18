# Music Diary Hackbright Project:

Music Diary is a social networking app for people who love to listen to and share music with others.  With Music Diary, users can create an account, login and start posting about music. Each post is created using the Spotify API’s search query where a user selects a song or album, writes their reaction/reflection/feeling about the music, then clicks post. Search for friends by username, like posts and use the clickable song, album and artist links to explore the musical taste of friends. I hope you enjoy using Music Diary, it was very fun to build.

![alt-text](https://github.com/rach0101/Music_Diary_Hackbright_Project/blob/main/GIF/Music%20Diary%20Gif.gif)

## Installation

First create a virtual environment and activate it.
``` bash 
virtualenv
```
``` bash
source/env/bin/activate
```
Install this project’s dependencies from the requirements.txt file.
Required dependencies include: Flask, Flask-SQLAlchemy, psycopg2-binary, Flask-DebugToolbar, requests, and Spotipy.

``` bash 
pip-3 install -r requirements.txt
```

You then will need to authenticate the Spotify API, I am using the [Spotipy Python library](https://spotipy.readthedocs.io/en/2.19.0/) to handle this. You will need to get a client ID, and Secret Key which I would recommend saving into a secrets.sh file. Go to [Spotify for Developers](https://developer.spotify.com/) and follow the instructions to [register your app](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app). 

``` bash 
touch secrets.sh 
```
Add the following code to your secrets.sh file. Once this is complete you are ready to use the app.

export SPOTIPY_CLIENT_ID=”YOUR CLIENT ID HERE”  
export SPOTIPY_CLIENT_SECRET=”YOUR SECRET KEY HERE”  
export APP_KEY=”YOUR APP KEY HERE”  


## Usage

Once you are set up and your virtual environment is activated, authenticate the Spotify API.
``` bash
source secrets.sh
```

Create all of the tables for the database by running seed_database.py. You only need to create the tables the first time you use the app.

```bash
python3 seed_database.py
```

Next run the server.

```bash
python3 server.py
```

Once the server is running you can use the app. Go to the home route to create an account, login and begin to post. Search for a song or album, click post music, write something about it in the text box and click post. 

Users can like their own posts and the posts of others. Search for others using the search bar at the top of the page. Make sure to search by username, other search queries will not render your friend’s page. If you want to go back to your diary, click the My Diary link in the navbar, and click logout to log yourself out.

Users can also delete their own posts. For now I have not implemented an edit post feature, so if you make a mistake you will have to delete and recreate your post.

## Files
There are 4 main Python files for the project which I will walk through:

### Model.py
This is where the classes for data tables are created.

### Seed_Database.py

This file automates dropping databases, creating databases and creating all tables.

### Crud.py 

Create, Read, Update, Delete: The functions in the crud file are used to create rows for our data tables, update the database and delete data.

### Server.py 

The server has all of the necessary routes to render HTML templates on the frontend, get data from the Spotify API, load the correct data onto user pages, log users in, create accounts and log users out. Server.py also handles like and delete post 
features.
