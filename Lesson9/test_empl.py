import pytest
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from company import Base, engine, SessionLocal

# Create a new database session for each test
@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

# Test configuration
BASE_URL = "https://x-clients-be.onrender.com"

def test_create_employee(db_session):
    response = requests.post(f"{BASE_URL}/employee", json={
        "is_active": True,
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "M",
        "phone": "1234567890",
        "email": "john.doe@example.com",
        "avatar_url": "http://example.com/avatar.jpg",
        "company_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"

def test_read_employee(db_session):
    response = requests.get(f"{BASE_URL}/employee/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_update_employee(db_session):
    response = requests.patch(f"{BASE_URL}/employee/1", json={
        "phone": "0987654321"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["phone"] == "0987654321"

def test_delete_employee(db_session):
    response = requests.delete(f"{BASE_URL}/employee/1")
    assert response.status_code == 200
    # Verify the employee is deleted
    response = requests.get(f"{BASE_URL}/employee/1")
    assert response.status_code == 404