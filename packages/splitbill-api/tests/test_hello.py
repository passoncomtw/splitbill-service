import unittest
from flask_testing import TestCase
from app import app
from flask.testing import FlaskClient


class Test_Hello(TestCase):
    def create_app(self):
        self.client: FlaskClient = None
        return app

    def test_hello_200(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code, 200)

        return response


if __name__ == "__main__":
    unittest.main()
