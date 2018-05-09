from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")

class RegisterForm(FlaskForm):
    name =  StringField("Nimi",[validators.length(1, 143, "Lisää nimi")])
    phonenumber =  StringField("Puhelinnumero",[validators.length(7, 143, "Lisää numero")])
    email =  EmailField("Sähköposti",[validators.length(6, 143, "Lisää sähköposti")])

    company =  StringField("Yritys",[validators.length(1, 143, "Lisää yrityksen nimi")])
    address =  StringField("Osoite",[validators.length(1, 143, "Lisää osoite")])

    username = StringField("käyttäjänimi",[validators.length(1, 143, "Lisää tunnus")])
    password = PasswordField("Salasana (vähintään 6 merkkiä)",[validators.length(6, 143, "Salasanan täytyy olla vähintään kuusi merkkiä")])

class PersonalForm(FlaskForm):
    name =  StringField("Nimi",[validators.length(1, 143, "lisää nimi")])
    phonenumber =  StringField("Puhelinnumero",[validators.length(1, 143, "lisää numero")])
    email =  EmailField("Sähköposti",[validators.length(6, 143, "lisää sähköposti")])

    company =  StringField("Yrityksen nimi",[validators.length(1, 143, "Lisää yrityksen nimi")])
    address =  StringField("Osoite",[validators.length(1, 143, "Lisää osoite")])

    password = StringField("Salasana (vähintään 6 merkkiä)",[validators.length(6, 1000, "Salasanan täytyy olla vähintään kuusi merkkiä")])
    