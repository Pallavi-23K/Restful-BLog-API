# blog_api/tests/test_auth.py

def test_register_and_login(client):
    # Register a new user
    r = client.post("/register", json={
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret"
    })
    assert r.status_code == 201
    assert r.get_json()["message"] == "User registered successfully!"

    # Login with the same user
    r = client.post("/login", json={
        "email": "alice@example.com",
        "password": "secret"
    })
    assert r.status_code == 200
    data = r.get_json()
    assert "access_token" in data


def test_duplicate_register(client):
    # First register
    client.post("/register", json={
        "username": "bob",
        "email": "bob@example.com",
        "password": "pw"
    })

    # Try registering again with the same email
    r = client.post("/register", json={
        "username": "bob2",
        "email": "bob@example.com",
        "password": "pw"
    })
    assert r.status_code == 400
    assert "already exists" in r.get_json()["error"].lower()
