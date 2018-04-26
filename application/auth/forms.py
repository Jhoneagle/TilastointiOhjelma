from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import validators, ValidationError
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

class RegisterForm(FlaskForm):
    name =  StringField("nimi",[validators.length(1, 1000, "lisää nimi")])
    phonenumber =  StringField("puhelin numero",[validators.length(1, 1000, "lisää numero")])
    email =  StringField("sähköposti",[validators.length(1, 1000, "lisää sähköposti")])

    company =  StringField("yritys",[validators.length(1, 1000, "lisää yrityksen nimi")])
    address =  StringField("osoite",[validators.length(1, 1000, "lisää osoite")])

    username = StringField("Username",[validators.length(1, 1000, "lisää tunnus")])
    password = PasswordField("Password",[validators.length(6, 1000, "salasanan täytyy olla vähintään kuusi merkkiä")])

class PersonalForm(FlaskForm):
    name =  StringField("nimi",[validators.length(1, 1000, "lisää nimi")])
    phonenumber =  StringField("puhelin numero",[validators.length(1, 1000, "lisää numero")])
    email =  StringField("sähköposti",[validators.length(1, 1000, "lisää sähköposti")])

    company =  StringField("yritys",[validators.length(1, 1000, "lisää yrityksen nimi")])
    address =  StringField("osoite",[validators.length(1, 1000, "lisää osoite")])

    password = StringField("Password",[validators.length(6, 1000, "salasanan täytyy olla vähintään kuusi merkkiä")])
    