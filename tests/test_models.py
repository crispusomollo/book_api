# tests/test_models.py
import unittest
from app import app
from models import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        app.create_all()

    def tearDown(self):
        app.session.remove()
        app.drop_all()

    def test_create_user(self):
        user = User(username='testuser', email='testuser@example.com')
        app.session.add(user)
        app.session.commit()
        queried_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, 'testuser@example.com')

if __name__ == '__main__':
    unittest.main()

