import pytest
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from empl_db import Employee
from company import Base, SessionLocal

DATABASE_URL = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
BASE_URL = "https://x-clients-be.onrender.com"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    Base.metadata.drop_all(bind=engine)
    session.close()

@pytest.fixture(scope="module")
def create_test_employee(db):
    employee = Employee(
        first_name="Nick",
        last_name="Plo",
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

def test_create_employee():
    response = requests.post(f"{BASE_URL}/employee", json={
        "first_name": "Ann",
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
    response = requests.patch(f"{BASE_URL}/employee/{employee_id}", json={
        "is_active": False
    })
    assert response.status_code == 200
    response = requests.get(f"{BASE_URL}/employee/{employee_id}")
    assert response.status_code == 404