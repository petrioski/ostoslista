from application import db


listPurchase = db.Table('listPurchase',
    db.Column('purchase_id', db.Integer, db.ForeignKey('purchase.id'), nullable=False),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), nullable=False)
)