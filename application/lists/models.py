from application import db
from application.models import Base

class List(Base):
    name = db.Column(db.String(500), nullable = False)
    done = db.Column(db.Boolean, nullable = False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    purchases = db.relationship("Purchase", secondary="list_purchase")

    def __init__(self, name):
        self.name = name
        self.done = False
