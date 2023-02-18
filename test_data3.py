
import unittest
import json
from app import app

class TestGetUsers(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(len(data), 3)

        user1 = data[0]
        self.assertEqual(user1['id'], 1)
        self.assertEqual(user1['name'], 'Alice')
        self.assertEqual(user1['age'], 25)

        user2 = data[1]
        self.assertEqual(user2['id'], 2)
        self.assertEqual(user2['name'], 'Bob')
        self.assertEqual(user2['age'], 30)

        user3 = data[2]
        self.assertEqual(user3['id'], 3)
        self.assertEqual(user3['name'], 'Charlie')
        self.assertEqual(user3['age'], 35)