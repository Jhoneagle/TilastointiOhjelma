""" routes """

from flask import render_template
from application import app

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Essi Esimerkki"

lista = [1, 1, 2, 3, 5, 8, 11]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Kolmas"))
esineet.append(Item("Neljäs"))

@app.route('/')
def home():
    return render_template("index.html", title='Index')

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet, title='Demo')