 # import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt
 # create a new instance of Flask and store it in app 
app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from os import getenv
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
login_manager.login_view = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))
db = SQLAlchemy(app)

from application import routes
