from application import db
from application.models import Base

class Kavijat(Base):
    
    __tablename__ = "kavijat"

    sivu_id = db.Column(db.Integer, db.ForeignKey('sivu.id'))

    kaynnit = db.Column(db.Integer, nullable=False)
    vuosi = db.Column(db.String(144), nullable=False)
    kuukausi = db.Column(db.String(144), nullable=False)

    kayttis = db.relationship("Kayttis", backref='kaivjat')
    selain = db.relationship("Selain", backref='kaivjat')

    def __init__(self, kaynnit, vuosi, kuukausi):
        self.kaynnit = kaynnit
        self.vuosi = vuosi
        self.kuukausi = kuukausi