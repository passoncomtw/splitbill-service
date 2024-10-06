import pytest
from app import create_app
from models import db
from config import Test_Config
from seeds import seed_data
from pytest_postgresql import factories
from pytest_postgresql.janitor import DatabaseJanitor

test_db = factories.postgresql_proc(port=None, dbname="test_db")


@pytest.fixture(scope="session")
def app(test_db):
    pg_host = test_db.host
    pg_port = test_db.port
    pg_user = test_db.user
    pg_password = test_db.password
    pg_db = test_db.dbname

    with DatabaseJanitor(
        user=pg_user,
        host=pg_host,
        port=pg_port,
        dbname=pg_db,
        version=test_db.version,
        password=pg_password,
    ):

        Test_Config.SQLALCHEMY_DATABASE_URI = (
            f"postgresql+psycopg2://{pg_user}:@{pg_host}:{pg_port}/{pg_db}"
        )

        app = create_app(Test_Config)

        with app.app_context():
            db.create_all()
            seed_data(db)

            yield app

        with app.app_context():
            db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()
