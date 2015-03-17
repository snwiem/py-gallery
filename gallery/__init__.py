__author__ = 'snwiem'

from flask import Flask
#from flask.ext.login import LoginManager
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('gallery.defaults')
#db = SQLAlchemy(app)
#lm = LoginManager(app)

#from model import User
from routes import *

#lm.login_view = 'login'
#db.create_all()