from application import db
from application.models import Base

class Kayttis(Base):
    
    __tablename__ = "kayttis"

    kavijat_id = db.Column(db.Integer, nullable=False)

    kaynnit = db.Column(db.Integer, nullable=False)
    kayttis = db.Column(db.String(144), nullable=False)
    
    def __init__(self, kaynnit, kayttis):
        self.kaynnit = kaynnit
        self.kayttis = kayttis