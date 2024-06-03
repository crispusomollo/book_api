import unittest
from api.v1.app import app
from models.book import Book
from bson.objectid import ObjectId
import json

class TestBooksAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_create_book(self):
        response = self.client.post('/get_items/', json={
            'title': 'Sample Book',
            'author': 'Author Name',
            'published_date': '2023-01-01',
            'isbn': '123-456-789',
            'pages': 300,
            'cover': 'https://example.com/cover.jpg',
            'language': 'English'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('_id', response.get_json())

    def test_get_all_books(self):
        response = self.client.get('/get_items/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_get_book(self):
        # Create a book first
        book_id = Book.create({
            'title': 'Sample Book',
            'author': 'Author Name'
        })
        response = self.client.get(f'/get_item/{book_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['_id'], str(book_id))

    def test_update_book(self):
        # Create a book first
        book_id = Book.create({
            'title': 'Sample Book',
            'author': 'Author Name'
        })
        response = self.client.put(f'/get_item/{book_id}', json={
            'title': 'Updated Sample Book'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Book updated')

    def test_delete_book(self):
        # Create a book first
        book_id = Book.create({
            'title': 'Sample Book',
            'author': 'Author Name'
        })
        response = self.client.delete(f'/get_item/{book_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Book deleted')

if __name__ == '__main__':
    unittest.main()

