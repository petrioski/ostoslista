from application import db
from application.models import Base
from sqlalchemy.sql import text


class Purchase(Base):
    amount = db.Column(db.Float, nullable=False)
    collected = db.Column(db.Boolean, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    list_id = db.Column(
        db.Integer,
        db.ForeignKey("list.id", ondelete="cascade"),
        nullable=False,
    )

    def __init__(self, amount):
        self.amount = amount
        self.collected = False

    @staticmethod
    def get_postgres_categories(purchase_list):
        ids = [p.item_id for p in purchase_list]
        stmt = text(
            "SELECT category.name "
            " FROM item "
            " LEFT JOIN category "
            "  ON item.category_id = category.id "
            " WHERE item.id = ANY(:id) "
            " GROUP BY category.name "
        ).params(id=ids)

        res = db.engine.execute(stmt)

        categories = []
        for row in res:
            categories.append(row[0])

        return categories

    @staticmethod
    def get_sqlite_categories(purchase_list):
        unique_categories = set()
        categories = []

        for i in purchase_list:
            stmt = text(
                "SELECT category.name "
                "FROM item "
                "LEFT JOIN category "
                " ON item.category_id = category.id "
                "WHERE item.id = :id"
            ).params(id=i.item_id)

            res = db.engine.execute(stmt).first()
            if not res[0] in unique_categories:
                categories.append(res[0])
                unique_categories.add(res[0])

        return categories

    @staticmethod
    def get_purchase_history(user_id):
        stmt = text("""
                SELECT item.name, count(purchase.id) as purchase_times
                FROM purchase
                LEFT JOIN item
                    ON purchase.item_id = item.id
                LEFT JOIN list
                    ON purchase.list_id = list.id
                WHERE
                    list.account_id = :id
                GROUP BY
                    item.name
                ORDER BY count(purchase.id) DESC
                """).params(id=user_id)
        res = db.engine.execute(stmt)
        response = list()

        for row in res:
            response.append(
                {"name": row[0], "purchase_count": row[1]}
            )

        return response
