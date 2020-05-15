from application import db

class List(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(500), nullable = False)
    valmis = db.Column(db.Boolean, nullable = False)

    def __init__(self, name):
        self.name = name
        self.valmis = False
