import unittest
from api.v1.app import app
from models.user import User
from bson.objectid import ObjectId
import json

class TestUsersAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_create_user(self):
        response = self.client.post('/get_users/', json={
            'name': 'Sample User',
            'email': 'user@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('_id', response.get_json())

    def test_get_all_users(self):
        response = self.client.get('/get_users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_user(self):
        # Create a user first
        user_id = User.create({
            'name': 'Sample User',
            'email': 'user@example.com'
        })
        response = self.client.get(f'/get_user/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['_id'], str(user_id))

    def test_update_user(self):
        # Create a user first
        user_id = User.create({
            'name': 'Sample User',
            'email': 'user@example.com'
        })
        response = self.client.put(f'/get_user/{user_id}', json={
            'name': 'Updated Sample User'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'User updated')

    def test_delete_user(self):
        # Create a user first
        user_id = User.create({
            'name': 'Sample User',
            'email': 'user@example.com'
        })
        response = self.client.delete(f'/get_user/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'User deleted')

if __name__ == '__main__':
    unittest.main()

