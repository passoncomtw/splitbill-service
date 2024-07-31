from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields

app = Flask(__name__)

db = initalDatabase(app)

api = Api(app)
api.prefix = '/api'

fakeDatabase = {
  1:{'name':'Clean car'},
  2:{'name':'Write blog'},
  3:{'name':'Start stream'},
}

taskFields = {
    'id':fields.Integer,
    'name':fields.String,
 }

class Items(Resource):
  def get(self):
    return fakeDatabase
  @marshal_with(taskFields)
  def post(self):
    data = request.json
    itemId = len(fakeDatabase.keys()) + 1
    fakeDatabase[itemId] = {'name':data['name']}
    return fakeDatabase

class Item(Resource):
  @marshal_with(taskFields)
  def get(self, pk):
    return fakeDatabase[pk]
  @marshal_with(taskFields)
  def put(self, pk):
    data = request.json
    fakeDatabase[pk]['name'] = data['name']
    return fakeDatabase
  @marshal_with(taskFields)
  def delete(self, pk):
    del fakeDatabase[pk]
    return fakeDatabase

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(80), unique=True, nullable=False)
#   email = db.Column(db.String(120), unique=True, nullable=False)

#   def __repr__(self):
#     return '<User %r>' % self.username
  
if __name__ == "__main__":
  app.run()