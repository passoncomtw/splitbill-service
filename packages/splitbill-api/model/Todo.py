from app import db

class Task(db.Model):
  __tablename__="tasks"
  
  id = db.Column(db.Integer, primary_key=True)
  
  createdAt = db.Column(db.DateTime, default=datetime.now, name="created_at")
  updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, name="updated_at")
  deletedAt = db.Column(db.DateTime, default=None, nullable=True)