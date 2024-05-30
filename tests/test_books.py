import unittest
from app import app

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_book(self):
        response = self.app.post('/books', json={"title": "Test Book", "author": "Author", "user_id": "123"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Book created successfully", str(response.data))

    def test_get_book(self):
        self.app.post('/books', json={"title": "Test Book", "author": "Author", "user_id": "123"})
        response = self.app.get('/books/Test Book')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Book", str(response.data))

if __name__ == '__main__':
    unittest.main()

