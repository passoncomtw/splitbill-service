from models import db
from sqlalchemy import Column, Integer, String, TIMESTAMP, func


class Groups(db.Model):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    user_count = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def __init__(self, name, user_count):
        self.name = name
        self.user_count = user_count

    def __repr__(self):
        return "<Group %r>" % self.name
