
import unittest
import json
from app import app

class TestGetUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        users = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(users), 3)

        user1 = {'id': 1, 'name': 'Alice', 'age': 25}
        user2 = {'id': 2, 'name': 'Bob', 'age': 30}
        user3 = {'id': 3, 'name': 'Charlie', 'age': 35}

        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)