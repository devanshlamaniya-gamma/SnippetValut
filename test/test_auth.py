import pytest
from fastapi.testclient import TestClient

# def test_login_user(client , test_user_data):

#     response = client.post(
#         "/router/login",
#         json = test_user_data
#     )

#     assert response.status_code == 200
#     assert "access_token" in response.json()


def test_login_user(client, registered_user):

    response = client.post(
        "/router/login",
        data={
            "username": registered_user["user_email"],
            "password": registered_user["password"],
        },
    )

    assert response.status_code == 200


def test_get_all_users(client, auth_token):

    response = client.get(
        "/router/users", json=test_login_user(client, test_user_data=test_login_user)
    )
    assert response.status_code == 200
    return response.json()
