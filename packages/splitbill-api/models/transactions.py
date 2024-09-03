from models import db
from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP, ForeignKey, func
from uuid import uuid4


class Transactions(db.Model):
    __tablename__ = "transactions"

    id = Column(
        String(36),
        autoincrement=False,
        default=lambda: str(uuid4()),
        primary_key=True,
        unique=True
    )
    group_id = Column(Integer,ForeignKey('groups.id'), nullable=False)
    from_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    to_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(DECIMAL, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __init__(self, group_id, from_user, to_user, amount):
        self.group_id = group_id
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def __repr__(self):
        return "<transactions %r>" % self.id
