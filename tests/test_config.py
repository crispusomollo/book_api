import unittest
from app import app
from config import TestConfig

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfig)
        self.app = app.test_client()

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()

