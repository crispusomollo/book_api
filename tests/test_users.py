import unittest
from api.v1.app import create_app
from models.user import mongo

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
        mongo.init_app(self.app)

        with self.app.app_context():
            mongo.db.users.delete_many({})

    def test_create_user(self):
        response = self.client.post('/api/v1/users', json={
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_user(self):
        self.client.post('/api/v1/users', json={
            'username': 'testuser',
            'password': 'password123'
        })
        response = self.client.get('/api/v1/users/testuser')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        self.client.post('/api/v1/users', json={
            'username': 'testuser',
            'password': 'password123'
        })
        response = self.client.put('/api/v1/users/testuser', json={
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        self.client.post('/api/v1/users', json={
            'username': 'testuser',
            'password': 'password123'
        })
        response = self.client.delete('/api/v1/users/testuser')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

