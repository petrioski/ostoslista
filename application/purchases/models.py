from application import db

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    amount = db.Column(db.Integer, nullable = False)
    collected = db.Column(db.Boolean, nullable = False)
    # TODO: item = foreign_key_for_item

    def __init__(self, amount):
        self.amount = amount
        self.collected = False 
