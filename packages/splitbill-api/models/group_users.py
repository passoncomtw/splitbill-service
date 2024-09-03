from models import db
from sqlalchemy import Column, Integer, ForeignKey

class Group_Users(db.Model):
    __tablename__ = "group_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.id"), primary_key=True, autoincrement=False
    )
    group_id = Column(
        Integer, ForeignKey("groups.id"), primary_key=True, autoincrement=False
    )

    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

    def __repr__(self):
        return "<Group_Users %r>" % self.group_id
