from application import db

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    osoite = db.Column(db.String(144), nullable=False)
    kuukausi = db.Column(db.Integer, nullable=False)
    vuosi = db.Column(db.Integer, nullable=False)

def __init__(self, osoite, kuukausi, vuosi):
    self.osoite = osoite
    self.kuukausi = kuukausi
    self.vuosi = vuosi