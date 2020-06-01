from application import db
from application.models import Base


class Category(Base):

    name = db.Column(db.String(500), nullable=False)

    items = db.relationship("Item", backref="category", lazy=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_items_per_category():
        stmt = """SELECT a.name, a.id, COUNT(b.id) as item_count
                  FROM category as a
                  LEFT JOIN item as b
                    ON a.id = b.category_id
                  GROUP BY a.name, a.id
                  ORDER BY COUNT(b.id) DESC, a.name
                """
        res = db.engine.execute(stmt)

        response = list()

        for row in res:
            response.append(
                {"name": row[0], "id": row[1], "item_count": row[2]}
            )

        return response
