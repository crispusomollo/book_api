# book_api/tests/test_books.py

import unittest
from api.v1.app import create_app

class BooksTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_get_all_books(self):
        response = self.client.get('/api/v1/books')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.client.post('/api/v1/books', json={"id": 1, "title": "Sample Book", "author": "Author"})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

