from application import db

class Sivu(db.Model):
    
    __tablename__ = "sivu"

    id = db.Column(db.Integer, primary_key=True)
    osoite = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)   

    visit = db.relationship("Visit", backref='sivu', lazy=True)

    def __init__(self, osoite):
        self.osoite = osoite