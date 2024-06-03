import pytest
from api.v1.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/api/v1/users/', json={
        'name': 'Sample User',
        'email': 'user@example.com'
    })
    assert response.status_code == 201

def test_get_all_users(client):
    response = client.get('/api/v1/users/')
    assert response.status_code == 200

def test_get_user(client):
    user_id = 'some_existing_user_id'  # replace with an actual user ID from your DB
    response = client.get(f'/api/v1/users/{user_id}')
    assert response.status_code == 200 or response.status_code == 404

