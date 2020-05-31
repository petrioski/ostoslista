from application import db


listPurchase = db.Table('user_list',
    db.Column('user_id', db.Integer, db.ForeignKey('account.id'), nullable=False),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), nullable=False)
)