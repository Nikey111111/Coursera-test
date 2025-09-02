import pytest
from app import app as flask_app
import json

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_login_success(client):
    response = client.post('/api/login', 
                          data=json.dumps({'username': 'admin', 'password': 'password123'}),
                          content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['success'] == True

def test_login_failure(client):
    response = client.post('/api/login', 
                          data=json.dumps({'username': 'admin', 'password': 'wrongpassword'}),
                          content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['success'] == False

