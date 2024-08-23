import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_purchase(browser):
    # Открытие страницы магазина
    browser.get('https://www.saucedemo.com/')

    # Авторизация
    username_input = browser.find_element(By.ID, 'user-name')
    password_input = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')
    login_button.click()

    # Добавление товаров в корзину
    products = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
    for product in products:
        add_button = browser.find_element(By.XPATH, f'//div[text()="{product}"]/ancestor::div[@class="inventory_item"]//button')
        add_button.click()

    # Переход в корзину
    cart_button = browser.find_element(By.ID, 'shopping_cart_container')
    cart_button.click()

    # Начало оформления заказа
    checkout_button = browser.find_element(By.ID, 'checkout')
    checkout_button.click()

    # Заполнение формы
    first_name_input = browser.find_element(By.ID, 'first-name')
    last_name_input = browser.find_element(By.ID, 'last-name')
    postal_code_input = browser.find_element(By.ID, 'postal-code')
    continue_button = browser.find_element(By.ID, 'continue')

    first_name_input.send_keys('Николай')
    last_name_input.send_keys('Плотников')
    postal_code_input.send_keys('123456')
    continue_button.click()

    # Чтение итоговой стоимости
    total_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label'))
    )
    total_text = total_element.text

    # Закрытие браузера
    browser.quit()

    # Проверка итоговой стоимости
    assert '$58.29' in total_text, f"Expected total to be '$58.29', but got '{total_text}'"