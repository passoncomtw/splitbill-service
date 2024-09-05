from flask import Flask
from flask_restx import Api, Resource, Namespace, fields
from models import db, migrate, users, groups, group_users, transactions
from models.users import Users, User_Scheme, Users_Scheme_Adapter
from config import Config
from seeds import seed_data


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db, compare_type=False, render_as_batch=False)

    api = Api(
        app,
        version="0.0",
        title="Split bill API",
        description="拆帳系統 API",
        doc="/doc",
    )

    users_api = Namespace("Users")

    users_model = api.model(
        "Users",
        {
            "id": fields.Integer(
                readonly=True, description="The task unique identifier"
            ),
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

            if user == None:
                return "User not found", 404

            user_dict = User_Scheme.model_validate(user).model_dump()

            return user_dict

    api.add_namespace(users_api, "/users")

    return app


app = create_app(Config)


@app.cli.command()
def seed():
    seed_data(db)


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
