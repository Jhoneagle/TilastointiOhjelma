from application import db
from application.models import Base

class Selain(Base):
    
    __tablename__ = "selain"

    kavijat_id = db.Column(db.Integer, db.ForeignKey('kavijat.id'))

    kaynnit = db.Column(db.Integer, nullable=False)
    selain = db.Column(db.String(144), nullable=False)
    
    def __init__(self, kaynnit, selain):
        self.kaynnit = kaynnit
        self.selain = selain