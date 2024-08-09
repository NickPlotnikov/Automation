import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_calculator(browser):
    # Открытие страницы калькулятора
    browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # Установка задержки
    delay_input = browser.find_element(By.XPATH, "//input[@id='delay']")
    delay_input.clear()
    delay_input.send_keys('45')

    # Нажатие на кнопки калькулятора
    button_7 = browser.find_element(By.XPATH, "//span[text()='7']")
    button_plus = browser.find_element(By.XPATH, "//span[text()='+']")
    button_8 = browser.find_element(By.XPATH, "//span[text()='8']")
    button_equals = browser.find_element(By.XPATH, "//span[text()='=']")

    button_7.click()
    button_plus.click()
    button_8.click()
    button_equals.click()

    # Ожидание результата в течение 50 секунд
    result = WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
    )

    # Проверка результата
    display_value = browser.find_element(By.CSS_SELECTOR, '.screen').text
    assert display_value == '15', f"Expected result '15', but got '{display_value}'"