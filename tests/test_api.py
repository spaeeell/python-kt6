import os

os.environ["DATABASE_URL"] = "sqlite:///./test_ci.db"
os.environ["SECRET_KEY"] = "test-only-secret-key-for-ci"

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200


def test_profile_without_token():
    response = client.get("/profile")
    assert response.status_code == 401
