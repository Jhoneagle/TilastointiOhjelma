""" initialiser """

from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webdata.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

import application.control

from application.visits import models
from application.visits import views

db.create_all()