from application import db
from application.models import Base

class Purchase(Base):
    amount = db.Column(db.Integer, nullable = False)
    collected = db.Column(db.Boolean, nullable = False)
    # TODO: item = foreign_key_for_item
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    listPurchases = db.relationship("listPurchase", backref='purchase', lazy=True)
    # list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

    def __init__(self, amount):
        self.amount = amount
        self.collected = False
