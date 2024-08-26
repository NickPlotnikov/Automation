import requests
import pytest
from db3 import get_db

BASE_URL = "https://x-clients-be.onrender.com/employee"

@pytest.fixture(scope="module")
def test_data():
    # Создание тестовой записи
    new_employee = {
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "Smith",
        "phone": "1234567890",
        "email": "john@example.com",
        "avatar_url": "http://example.com/avatar.jpg",
        "company_id": 1
    }
    
    response = requests.post(BASE_URL, json=new_employee)

    assert response.status_code == 201

    yield response.json()  # Возвращаем данные для использования в тестах

    # Удаление тестовой записи после выполнения тестов
    if 'id' in response.json():
        employee_id = response.json()['id']
        requests.patch(f"{BASE_URL}/{employee_id}", json={"is_active": False})


def test_get_employee(test_data):
    response = requests.get(f"{BASE_URL}/{test_data['id']}")
    assert response.status_code == 200
    assert response.json()['first_name'] == "John"


def test_patch_employee(test_data):
    update_data = {
        "first_name": "Jane"
    }
    response = requests.patch(f"{BASE_URL}/{test_data['id']}", json=update_data)
    assert response.status_code == 200
    
    # Проверка обновления
    response = requests.get(f"{BASE_URL}/{test_data['id']}")
    assert response.json()['first_name'] == "Jane"


def test_delete_employee(test_data):
    response = requests.patch(f"{BASE_URL}/{test_data['id']}", json={"is_active": False})
    assert response.status_code == 200
    
    response = requests.get(f"{BASE_URL}/{test_data['id']}")
    assert response.status_code == 404  # Запись должна быть не найдена