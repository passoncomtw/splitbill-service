from flask import Flask
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
api = Api(
    app, version="0.0", title="Split bill API", description="拆帳系統 API", doc="/doc"
)

todo_api = Namespace("To Do")


class To_Do_Store:
    def __init__(self):
        self.__list = []
        self.__last_id = 0

    def get_all(self):
        return self.__list

    def get(self, id):
        for todo in self.__list:
            if todo["id"] == id:
                return todo

        return None

    def create(self, *, name):
        self.__last_id += 1
        new_todo = {"id": self.__last_id + 1, "name": name}

        self.__list.append(new_todo)
        return new_todo

    def update(self, *, id, name):
        todo = self.get(id)

        if todo is None:
            return None

        todo.update({"id": id, "name": name})
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.__list.remove(todo)


todo_store = To_Do_Store()

todo_store.create(name="todo 1")
todo_store.create(name="todo 2")
todo_store.create(name="todo 3")


todo_model = api.model(
    "Todo",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "name": fields.String(required=True, description="The task details"),
    },
)


@todo_api.route("")
class To_Do_List(Resource):
    def get(self):
        return todo_store.get_all()

    @todo_api.expect(todo_model)
    def post(self):
        todo = todo_store.create(name=api.payload["name"])

        if todo is None:
            return "Todo not found", 404

        return todo


@todo_api.route("/<int:id>")
@todo_api.response(404, "Todo not found")
class To_Do(Resource):
    def get(self, id):
        todo = todo_store.get(id)

        if todo is None:
            return "Todo not found", 404

        return todo

    def delete(self, id):
        todo_store.delete(id)
        return "", 204

    @todo_api.expect(todo_model)
    def put(self, id):
        todo = todo_store.update(id=id, name=todo_api.payload["name"])

        if todo is None:
            return "Todo not found", 404

        return todo


api.add_namespace(todo_api, "/todos")


@app.cli.command()
def test():
    import unittest
    import sys

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
