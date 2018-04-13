from application import db
from application.models import Base

class Sivu(Base):
    
    __tablename__ = "sivu"

    osoite = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, nullable=False)
    ryhma = db.Column(db.String(144), nullable=False)

    visit = db.relationship("Visit", backref='sivu')

    def __init__(self, osoite, osoiteRyhma):
        self.osoite = osoite
        self.ryhma = osoiteRyhma