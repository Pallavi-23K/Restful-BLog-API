import pytest
from blog_api.main import create_app, db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_ENGINE_OPTIONS": {"connect_args": {"check_same_thread": False}},
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def auth_token(client):
    """Register a test user and return their JWT access token."""
    def _auth(username="testuser", email="test@example.com", password="secret"):
        # Register user
        client.post("/register", json={
            "username": username,
            "email": email,
            "password": password
        })
        # Login user
        response = client.post("/login", json={
            "email": email,
            "password": password
        })
        return response.get_json()["access_token"]
    return _auth
