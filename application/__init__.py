""" initialiser """

from flask import Flask
import os
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webdata.db"    
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import application.control

from application.visits import models
from application.visits import views

from application.auth import models
from application.auth import views

from application.kavijat import models
from application.kavijat import views

from application.selain import models

from application.kayttis import models

from application.yhteenveto import views

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass