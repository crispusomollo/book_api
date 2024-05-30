import unittest
from app import app

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', json={"username": "testuser", "email": "test@example.com"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("User created successfully", str(response.data))

    def test_get_user(self):
        self.app.post('/users', json={"username": "testuser", "email": "test@example.com"})
        response = self.app.get('/users/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn("testuser", str(response.data))

if __name__ == '__main__':
    unittest.main()

