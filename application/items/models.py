from application import db
from application.models import Base

class Item(Base):
    name = db.Column(db.String(500), nullable = False)
    unit_type = db.Column(db.String(144), nullable = False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    purchases = db.relationship("Purchase", backref='item', lazy=True)

    def __init__(self, name):
        self.name = name
