"""Automate dropping database, creating database and creating all tables"""

import os, json, model, crud, server 
from random import choice, randint
from datetime import datetime

#drop database and create new empty db
os.system('dropdb diary')
os.system('createdb diary')

#connect our app to db created
model.connect_to_db(server.app)

#use our models and create all the tables
#in the database
model.db.create_all()