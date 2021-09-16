"""Automate dropping database, creating database and creating all tables"""

import os, json, model, crud, server 
from random import choice, randint
from datetime import datetime

#Drop database and create new empty db
os.system('dropdb diary')
os.system('createdb diary')

#Connect my app to db created
model.connect_to_db(server.app)

#Use models to create all of the tables
#in the database
model.db.create_all()

