from application import db

class Sivu(db.Model):
    
    __tablename__ = "sivu"

    id = db.Column(db.Integer, primary_key=True)
    osoite = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, nullable=False)   

    visit = db.relationship("Visit", backref='sivu')

    def __init__(self, osoite):
        self.osoite = osoite