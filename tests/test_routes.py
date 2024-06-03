# tests/test_routes.py
import unittest
from app import app
from models import User

class UserRoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        app.create_all()

    def tearDown(self):
        app.session.remove()
        app.drop_all()

    def test_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_user(self):
        response = self.app.post('/api/v1/users', json={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 201)
        queried_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'testuser@example.com')

if __name__ == '__main__':
    unittest.main()

