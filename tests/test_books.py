import unittest
from api.v1.app import create_app
from models.book import mongo

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['MONGO_URI'] = 'mongodb://localhost:27017/testdb'
        mongo.init_app(self.app)

        with self.app.app_context():
            mongo.db.books.delete_many({})

    def test_create_book(self):
        response = self.client.post('/api/v1/books', json={
            'title': 'Test Book',
            'author': 'Author Name'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_book(self):
        book_id = str(mongo.db.books.insert_one({
            'title': 'Test Book',
            'author': 'Author Name'
        }).inserted_id)
        response = self.client.get(f'/api/v1/books/{book_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        book_id = str(mongo.db.books.insert_one({
            'title': 'Test Book',
            'author': 'Author Name'
        }).inserted_id)
        response = self.client.put(f'/api/v1/books/{book_id}', json={
            'title': 'Updated Title'
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        book_id = str(mongo.db.books.insert_one({
            'title': 'Test Book',
            'author': 'Author Name'
        }).inserted_id)
        response = self.client.delete(f'/api/v1/books/{book_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

