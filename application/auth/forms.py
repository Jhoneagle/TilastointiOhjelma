from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import validators, ValidationError
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

class RegisterForm(FlaskForm):
    name =  StringField("nimi",[validators.length(1, 1000, "lisää nimi")])
    username = StringField("Username",[validators.length(1, 1000, "lisää tunnus")])
    password = PasswordField("Password",[validators.length(1, 1000, "lisää salasana")])
    