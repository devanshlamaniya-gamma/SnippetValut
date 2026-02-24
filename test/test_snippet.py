def test_get_alll_snips(client , auth_token):
    
    response = client.get(
        "/snippets/get_all",
        headers={"Authorization" : f"Bearer {auth_token}"}
    )

    assert response.status_code== 200


# def test_get_snippet(client , test_snippet_id, auth_token):

#     response = client.get(
#         f"/snippets/snippet_{test_snippet_id["id"]}",
#         headers={"Authorization": f"Bearer {auth_token}"} )

#     assert response.status_code == 200
#     return response
