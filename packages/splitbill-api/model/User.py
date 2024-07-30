from app import db
from utils.crapto import hash_password

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	phone = db.Column(db.String(20))
	password = db.Column(db.String(120))
	createdAt = db.Column(db.DateTime, default=datetime.now, name="created_at")
	updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, name="updated_at")
	deletedAt = db.Column(db.DateTime, default=None, nullable=True)
	# todos = db.relationship('Todo', backref='user', lazy='select')

	def __init__(self, name, password, phone):
		self.name=name
		self.phone=phone
		self.password = hash_password(password)

	def __repr__(self):
		return 'Id: {}, name: {}'.format(self.id, self.name)
 