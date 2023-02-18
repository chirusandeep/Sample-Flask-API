
import unittest
import json
from app import app

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        expected_data = [{'id': 1, 'name': 'Alice', 'age': 25}, {'id': 2, 'name': 'Bob', 'age': 30}, {'id': 3, 'name': 'Charlie', 'age': 35}]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_data)