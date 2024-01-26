from fastapi.testclient import TestClient
from httpx import delete
from database import session_local
from main import app
from auth import create_acccess_token
from datetime import timedelta, datetime

client = TestClient(app)

def test_create_book():
    with TestClient(app) as client:
        jwt_token = create_acccess_token("shiva", 1, timedelta(minutes=20))

        response = client.post(
            "/books/",
            json={
                "isbn": 0,
                "title": "Sample Book",
                "author": "string",
                "price": 0,
                "quantity": 0,
            },
            headers={"Authorization": f"Bearer {jwt_token}"},
        )
        assert response.status_code == 201


def test_read_books():
    with TestClient(app) as client:
        response = client.get("/books/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


def test_read_book():
    with TestClient(app) as client:
        response = client.get("/book/5678")
        assert response.status_code == 200
        assert response.json()["isbn"] == 5678


def test_update_book():
    with TestClient(app) as client:
        jwt_token = create_acccess_token("shiva", 1, timedelta(minutes=20))
        response = client.put(
            "/book/5678",
            json={
                "isbn": 5678,
                "title": "Sample Book",
                "author": "string",
                "price": 0,
                "quantity": 0,
            },
            headers={"Authorization": f"Bearer {jwt_token}"},
        )
        assert response.status_code == 200


def test_delete_book():
    with TestClient(app) as client:
        jwt_token = create_acccess_token("shiva", 1, timedelta(minutes=20))
        response = client.delete(
            "/book/4567",
            headers={"Authorization": f"Bearer {jwt_token}"},
        )
        assert response.status_code == 200
