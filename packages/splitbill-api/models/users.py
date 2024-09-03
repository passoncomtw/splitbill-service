from models import db
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, ConfigDict, TypeAdapter
from typing import List


class Users(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=True)
    line_id = Column(String, nullable=False)
    user_tag = Column(String, nullable=False)

    groups = db.relationship("Group_Users", backref="users")
    
    def __init__(self, name, line_id, user_tag):
        self.name = name
        self.line_id = line_id
        self.user_tag = user_tag

    def __repr__(self):
        return "<User %r>" % self.name


# Pydantic models
class User_Scheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    line_id: str
    user_tag: str


Users_Scheme_Adapter = TypeAdapter(List[User_Scheme])
