# def test_login_user(client , test_user_data):

#     response = client.post(
#         "/router/login",
#         json = test_user_data
#     )

#     assert response.status_code == 200
#     assert "access_token" in response.json()


# def test_login_user(client, test_user_logindata):

#     response = client.post(
#         "/router/login",
#         data=test_user_logindata,
#     )

#     assert response.status_code == 200
#     assert "access_token" in response

def test_login_user(client, test_user_logindata,registered_user):
    # registered_user
    response = client.post(
        "/router/login",
        data={
            "username": test_user_logindata["user_name"],
            "password": test_user_logindata["password"]
        },
    )

    assert response.status_code == 200

def test_get_all_users(client, auth_token):

    response = client.get(
        "/router/users",
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200

