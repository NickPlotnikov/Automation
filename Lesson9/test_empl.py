import pytest
import requests

BASE_URL = "https://x-clients-be.onrender.com"

# Fixture to set up and tear down the database state
@pytest.fixture(scope="function")
def setup_db():
    # Create a new employee to be used in tests
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
    employee_id = response.json().get("id")
    yield employee_id
    # Clean up after tests
    requests.delete(f"{BASE_URL}/employee/{employee_id}")

def test_create_employee():
    response = requests.post(f"{BASE_URL}/employee", json={
        "is_active": True,
        "first_name": "Jane",
        "last_name": "Smith",
        "middle_name": "A",
        "phone": "0987654321",
        "email": "jane.smith@example.com",
        "avatar_url": "http://example.com/avatar2.jpg",
        "company_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Jane"

def test_read_employee(setup_db):
    employee_id = setup_db
    response = requests.get(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id

def test_update_employee(setup_db):
    employee_id = setup_db
    response = requests.patch(f"{BASE_URL}/employee/{employee_id}", json={
        "phone": "1122334455"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["phone"] == "1122334455"

def test_delete_employee(setup_db):
    employee_id = setup_db
    response = requests.delete(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 404