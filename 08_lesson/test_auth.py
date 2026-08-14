def test_auth_token_obtained_and_usable(auth_token, base_api_url):
    import requests
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {auth_token}"})

    me_resp = session.get(f"{base_api_url.replace('/api-v2', '')}/users/me")
    assert me_resp.status_code == 200
    me = me_resp.json()

    print(f"[DIAG] User: {me.get('name')}, Company: {me.get('company_name')}")
    assert "name" in me and "company_name" in me, "Недостаточно данных о пользователе"