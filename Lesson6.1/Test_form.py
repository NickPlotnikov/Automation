import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    # Путь к geckodriver (обновите этот путь в соответствии с вашим расположением geckodriver)
    geckodriver_path = '/path/to/geckodriver'

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Запуск браузера в режиме без графического интерфейса

    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)
    yield driver
    driver.quit()

def test_fill_and_submit_form(browser):
    # Открытие страницы
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    # Заполнение формы
    first_name = browser.find_element(By.NAME, 'firstName')
    first_name.send_keys('Иван')

    last_name = browser.find_element(By.NAME, 'lastName')
    last_name.send_keys('Петров')

    address = browser.find_element(By.NAME, 'address')
    address.send_keys('Ленина, 55-3')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('test@skypro.com')

    phone = browser.find_element(By.NAME, 'phoneNumber')
    phone.send_keys('+7985899998787')

    city = browser.find_element(By.NAME, 'city')
    city.send_keys('Москва')

    country = browser.find_element(By.NAME, 'country')
    country.send_keys('Россия')

    job_position = browser.find_element(By.NAME, 'jobPosition')
    job_position.send_keys('QA')

    company = browser.find_element(By.NAME, 'company')
    company.send_keys('SkyPro')

    # Оставляем поле Zip code пустым

    # Нажатие кнопки Submit
    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

    # Проверка подсветки полей
    def check_highlight(element):
        return "rgb(255, 0, 0)" in element.value_of_css_property('border-color')

    zip_code = browser.find_element(By.NAME, 'zipCode')
    assert check_highlight(zip_code), "Zip code field is not highlighted in red"

    other_fields = [
        first_name, last_name, address, email, phone, city, country, job_position, company
    ]
    for field in other_fields:
        assert "rgb(0, 128, 0)" in field.value_of_css_property('border-color'), f"{field.get_attribute('name')} field is not highlighted in green"