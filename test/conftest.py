import uuid

import pytest
from fastapi.testclient import TestClient

from app.main import app

# from main import app


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture
def test_user_data():
    return {
        "user_name": "devansh",
        "user_email": f"devansh{uuid.uuid4()}@gmail.com",
        "password": "Devansh@123",
    }


@pytest.fixture
def test_user_logindata():
    return {"email": "devansh@gmail.com", "password": "Devansh@123"}


@pytest.fixture
def registered_user(client, test_user_data):
    response = client.post("/router/create", json=test_user_data)

    assert response.status_code == 201
    return response.json()


@pytest.fixture
def auth_token(client, test_user_data, registered_user):
    response = client.post("/router/login", json=test_user_data)
    assert response.status_code == 200
    return response.json()["access_token"]
