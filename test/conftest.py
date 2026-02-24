import uuid

import pytest
from fastapi.testclient import TestClient

from app.main import app

# from main import app


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c

un_id = uuid.uuid4()
@pytest.fixture
def test_user_data():
    return {
        "user_name": f"devansh{un_id}",
        "user_email": f"devansh{un_id}@gmail.com",
        "password": "Devansh@123",
    }


@pytest.fixture
def test_user_logindata():
    return {"user_name": f"devansh{un_id}", "password": "Devansh@123"}


# @pytest.fixture
# def registered_user(client, test_user_data):
#     response = client.post("/router/create", json=test_user_data)

#     assert response.status_code == 200
#     return response





@pytest.fixture 
def registered_user(client, test_user_data): 
    response = client.post("/router/create", json=test_user_data) 
    if response.status_code == 422:

        print("\nValidation Error Details:", response.json()) 
    assert response.status_code == 200
    return response.json()
# @pytest.fixture
# def auth_token(client, test_user_logindata, registered_user):
#     response = client.post("/router/login", data=test_user_logindata)
#     assert response.status_code == 200
#     # return response.json()["access_token"]

@pytest.fixture
def auth_token(client, test_user_data):
    response = client.post(
        "/router/login",
        data={
            "username": test_user_data["user_name"],  
            "password": test_user_data["password"], 
        },
    )

    assert response.status_code == 200
    return response.json()["access_token"]


@pytest.fixture
def test_snippet_id():
    return {"id" : 1}

# like we make connection with db we need to manually close it every time think in 100 times
# function takes more time
# automatic use via conftest.py

# coverage run -m pytest
# converage report -m