import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep

@pytest.fixture(scope="module")
def browser():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_data_types_form(browser):
    fake = Faker('ru_RU')  # Для генерации данных на русском языке
    # Открытие страницы формы
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Генерация данных с использованием Faker
    form_data = {         
        'first-name': fake.first_name_male(),
        'last-name': fake.last_name_male(),
        'address': f"{fake.street_name()}, {fake.building_number()}",
        'e-mail': fake.email(),
        'phone': fake.phone_number(),
        'zip-code': '',  # Оставить пустым
        'city': fake.city(),
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
    }
    
    # Заполнение формы
    for field_name, value in form_data.items():
         browser.find_element(By.NAME, field_name).send_keys(value)
   
    # Нажатие на кнопку Submit
    WebDriverWait(browser, 40, 0.1).until(
         EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)    

    # Проверка, что поля подсвечены правильным цветом
    field_classes = {
            "zip-code": "danger",  # Красный
            "first-name": "success", 
            "last-name": "success", 
            "address": "success", 
            "e-mail": "success", 
            "phone": "success",
            "city": "success", 
            "country": "success", 
            "job-position": "success", 
            "company": "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in browser.find_element(
            By.ID, field_id).get_attribute("class")
        
if __name__ == "__main__":
    pytest.main()