import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_fill_and_submit_form(browser):
    # Открытие страницы
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Заполнение формы
    form_data = {
        'first-name': 'Иван',
        'last-name': 'Петров',
        'address': 'Ленина, 55-3',
        'e-mail': 'test@skypro.com',
        'phone': '+7985899998787',            
        'city': 'Москва',
        'country': 'Россия',
        'job-position': 'QA',
        'company': 'SkyPro'
    }

    for field, value in form_data.items():
        browser.find_element(By.NAME, field).send_keys(value)

    # Оставляем поле Zip code пустым

    # Нажатие кнопки Submit
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

    # Проверка подсветки полей
    zip_code = browser.find_element(By.NAME, 'zip-code')
    assert "rgb(255, 0, 0)" in zip_code.value_of_css_property('border-color'), "Zip code field is not highlighted in red"

    for field in form_data.Keys():
        element = browser.find_element(By.NAME, field)
        assert "rgb(0, 128, 0)" in element.value_of_css_property('border-color'), f"{field} field is not highlighted in green"