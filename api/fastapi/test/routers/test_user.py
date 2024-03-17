from sqlalchemy.orm import Session

from database.database import get_test_db_session
from dependencies import get_current_user, get_db
from fastapi.testclient import TestClient
from main import app


def override_get_db():
    SessionLocal = get_test_db_session()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    yield None


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


def test_user():
    response = client.post(
        "/users",
        json={
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Smith",
            "birthday": "1982-06-12",
            "password": "password",
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert "id" in data
    assert data["email"] == "test@example.com"
    assert data["first_name"] == "John"
    assert data["last_name"] == "Smith"
    assert data["birthday"] == "1982-06-12"
    assert data["is_active"] == True

    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == "test@example.com"
    assert data["first_name"] == "John"
    assert data["last_name"] == "Smith"
    assert data["birthday"] == "1982-06-12"
    assert data["is_active"] == True

    response = client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["id"] == user_id
    assert data[0]["email"] == "test@example.com"
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Smith"
    assert data[0]["birthday"] == "1982-06-12"
    assert data[0]["is_active"] == True

    response = client.put(
        f"/users/{user_id}",
        json={
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Smith",
            "birthday": "1982-06-12",
            "password": "password",
            "is_active": False,
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == user_id
    assert data["email"] == "test@example.com"
    assert data["first_name"] == "John"
    assert data["last_name"] == "Smith"
    assert data["birthday"] == "1982-06-12"
    assert data["is_active"] == False
