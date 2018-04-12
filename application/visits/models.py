from application import db
from application.models import Base

class Visit(Base):
    
    __tablename__ = "visit"

    kuukausi = db.Column(db.Integer, nullable=False)
    vuosi = db.Column(db.Integer, nullable=False)
    lukumaara = db.Column(db.Integer, nullable=False)

    sivu_id = db.Column(db.Integer, db.ForeignKey('sivu.id'))

def __init__(self, kuukausi, vuosi, lukumaara):
    self.kuukausi = kuukausi
    self.vuosi = vuosi
    self.lumaara = lukumaara