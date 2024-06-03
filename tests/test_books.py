import pytest
from api.v1.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_book(client):
    response = client.post('/api/v1/books/', json={
        'title': 'Sample Book',
        'author': 'Author Name'
    })
    assert response.status_code == 201

def test_get_all_books(client):
    response = client.get('/api/v1/books/')
    assert response.status_code == 200

def test_get_book(client):
    book_id = 'some_existing_book_id'  # replace with an actual book ID from your DB
    response = client.get(f'/api/v1/books/{book_id}')
    assert response.status_code == 200 or response.status_code == 404

