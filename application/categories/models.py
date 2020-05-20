from application import db
from application.models import Base

class Category(Base):

    name = db.Column(db.String(500), nullable = False)

    items = db.relationship("Item", backref='category', lazy=True)

    def __init__(self, name):
        self.name = name
