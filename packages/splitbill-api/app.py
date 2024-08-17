from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, version='0.0', title='Split bill API',
          description='拆帳系統 API',  doc='/doc')

hello = Namespace("Hello")


@hello.route("")
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


api.add_namespace(hello, '/hello')

if __name__ == '__main__':
    app.run()
