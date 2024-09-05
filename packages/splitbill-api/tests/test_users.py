import unittest
from flask_testing import TestCase
from app import app
from flask.testing import FlaskClient
import json
from seeds import user_data
from unittest.mock import patch
from models.users import Users
from models import db

class Test_Users(TestCase):
    def setUp(self):
        self.app.testing = True
  
    def create_app(self):
        self.client: FlaskClient = None
        return app

    @patch("models.users.Users.query.get")
    def test_get_user_success(self, mock_get):
        # def mock_query(user_id):
        #     return Users(**user_data["data"][0])

        # mock_get.side_effect = mock_query

        # 模擬一個用戶
        mock_user = Users(**user_data["data"][0])
        mock_get.return_value = mock_user

        # 執行 GET 請求
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 200)

    # def test_get_todos_200(self):
    #     response = self.client.get("/todos")
    #     self.assertEqual(response.status_code, 200)

    # def test_create_todo_200(self):
    #     response = self.client.post("/todos", json={"name": "hello task"})
    #     self.assertEqual(response.status_code, 200)

    # def test_update_todo_200(self):
    #     create_response = self.client.post("/todos", json={"name": "hello task"})
    #     create_data = json.loads(create_response.get_data(as_text=True))

    #     update_response = self.client.put(
    #         f"/todos/{create_data['id']}", json={"name": "hello task"}
    #     )
    #     update_data = json.loads(update_response.get_data(as_text=True))
    #     self.assertEqual(update_data["name"], "hello task")

    # def test_delete_todo_200(self):
    #     create_response = self.client.post("/todos", json={"name": "hello task"})
    #     create_data = json.loads(create_response.get_data(as_text=True))

    #     delete_response = self.client.delete(f"/todos/{create_data['id']}")
    #     self.assertEqual(delete_response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
