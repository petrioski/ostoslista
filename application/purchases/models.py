from application import db
from application.models import Base

class Purchase(Base):
    amount = db.Column(db.Integer, nullable = False)
    collected = db.Column(db.Boolean, nullable = False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    shopping_lists = db.relationship("List", secondary="list_purchase")


    def __init__(self, amount):
        self.amount = amount
        self.collected = False
