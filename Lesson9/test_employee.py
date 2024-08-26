import pytest
import requests
from sqlalchemy.orm import Session
from db import SessionLocal, Employee, engine

BASE_URL = "http://localhost:8000"  # Укажите правильный URL вашего API

@pytest.fixture(scope="module")
def db():
    # Создание новой сессии для каждого теста
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture(scope="module")
def create_test_employee(db):
    employee = Employee(
        first_name="John",
        last_name="Doe",
        middle_name="M",
        phone="1234567890",
        email="john.doe@example.com",
        avatar_url="http://example.com/avatar.jpg",
        company_id=1
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def test_create_employee(create_test_employee):
    response = requests.post(f"{BASE_URL}/employee", json={
        "first_name": "Alice",
        "last_name": "Smith",
        "middle_name": "A",
        "phone": "0987654321",
        "email": "alice.smith@example.com",
        "avatar_url": "http://example.com/alice_avatar.jpg",
        "company_id": 2
    })
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["first_name"] == "Alice"
    assert data["last_name"] == "Smith"

def test_read_employee(create_test_employee):
    employee_id = create_test_employee.id
    response = requests.get(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == create_test_employee.first_name
    assert data["last_name"] == create_test_employee.last_name

def test_update_employee(create_test_employee):
    employee_id = create_test_employee.id
    response = requests.patch(f"{BASE_URL}/employee/{employee_id}", json={
        "phone": "1112223333"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["phone"] == "1112223333"

def test_delete_employee(create_test_employee):
    employee_id = create_test_employee.id
    response = requests.delete(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 204
    # Проверим, что запись была удалена
    response = requests.get(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 404