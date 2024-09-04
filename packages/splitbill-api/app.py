from flask import Flask
from flask_restx import Api, Resource, Namespace, fields
from models import db, migrate, users, groups, group_users, transactions
from models.users import Users, User_Scheme, Users_Scheme_Adapter
from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://admin:123456@127.0.0.1:5436/splitbill_databas"
)

db.init_app(app)
migrate.init_app(app, db, compare_type=False, render_as_batch=False)

api = Api(
    app, version="0.0", title="Split bill API", description="拆帳系統 API", doc="/doc"
)

users_api = Namespace("Users")

users_model = api.model(
    "Users",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "name": fields.String(required=True, description="The task details"),
        "line_id": fields.String(required=True, description="The task details"),
        "user_tag": fields.String(required=True, description="The task details"),
    },
)


@users_api.route("")
class User_List(Resource):
    def get(self):
        users = Users.query.all()

        user_list = Users_Scheme_Adapter.dump_python(users)

        return user_list

    @users_api.expect(users_model)
    def post(self):
        new_user = Users(**users_api.payload)

        db.session.add(new_user)
        db.session.commit()

        return "create user success", 200


@users_api.route("/<int:id>")
@users_api.response(404, "User not found")
class User(Resource):
    def get(self, id):
        user = Users.query.get(id)
        user_dict = User_Scheme.model_validate(user).model_dump()

        return user_dict

    # def delete(self, id):
    #     todo_store.delete(id)
    #     return "", 204

    # @users_api.expect(todo_model)
    # def put(self, id):
    #     todo = todo_store.update(id=id, name=users_api.payload["name"])

    #     if todo is None:
    #         return "Todo not found", 404

    #     return todo


api.add_namespace(users_api, "/users")


@app.cli.command()
def seed():
    # load entities
    from seeds import data
    
    # Initializing Seeder
    seeder = Seeder(db.session)

    # Seeding
    seeder.seed(data)

    # Committing
    db.session.commit()  # or seeder.session.commit()


@app.cli.command()
def test():
    import unittest
    import sys

    tests = unittest.TestLoader().discover("tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)


if __name__ == "__main__":
    app.run()
