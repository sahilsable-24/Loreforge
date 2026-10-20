EMAIL = "hero@example.com"
PASSWORD = "correct-horse-battery"


def register(client, email=EMAIL, password=PASSWORD):
    return client.post("/auth/register", json={"email": email, "password": password})


def register_and_login(client, email=EMAIL, password=PASSWORD):
    register(client, email, password)
    res = client.post("/auth/login", json={"email": email, "password": password})
    assert res.status_code == 200
    return res.json()  # {"access_token": ..., "refresh_token": ...}


def refresh(client, refresh_token):
    return client.post("/auth/refresh", json={"refresh_token": refresh_token})


def test_register_succeeds(client):
    assert register(client).status_code == 201


def test_register_duplicate_email_conflicts(client):
    register(client)
    assert register(client).status_code == 409


def test_login_wrong_password_rejected(client):
    register(client)
    res = client.post("/auth/login", json={"email": EMAIL, "password": "wrong-password"})
    assert res.status_code == 401


def test_me_without_token_rejected(client):
    res = client.get("/auth/me")
    assert res.status_code in (401, 403)  # HTTPBearer may return either


def test_me_with_token_works(client):
    tokens = register_and_login(client)
    res = client.get("/auth/me", headers={"Authorization": f"Bearer {tokens['access_token']}"})
    assert res.status_code == 200
    assert res.json()["email"] == EMAIL


def test_refresh_rotates_tokens(client):
    tokens = register_and_login(client)
    first = refresh(client, tokens["refresh_token"])
    assert first.status_code == 200
    assert first.json()["refresh_token"] != tokens["refresh_token"]

    # the old token was used up, so it must fail now
    assert refresh(client, tokens["refresh_token"]).status_code == 401


def test_reuse_revokes_all_tokens(client):
    old = register_and_login(client)["refresh_token"]
    new = refresh(client, old).json()["refresh_token"]  # legit rotation

    assert refresh(client, old).status_code == 401  # "thief" replays old token
    assert refresh(client, new).status_code == 401  # real user's token is now dead too


def test_email_is_case_insensitive(client):
    register(client, email="Hero@Example.com ")
    res = client.post("/auth/login", json={"email": "HERO@example.COM", "password": PASSWORD})
    assert res.status_code == 200