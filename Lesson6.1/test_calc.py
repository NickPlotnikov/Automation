# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(scope="module")
# def browser():
#     driver = webdriver.Firefox()
#     yield driver
#     driver.quit()

# def test_calculator(browser):
#     # Открытие страницы
#     browser.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

#     # Ввод значения задержки
#     delay_input = browser.find_element(By.ID, 'delay')
#     delay_input.clear()
#     delay_input.send_keys('45')

#     # Нажатие на кнопки калькулятора
#     buttons = ['7', '+', '8', '=']
#     for button in buttons:
#         browser.find_element(By.XPATH, f'//button[text()="{button}"]').click()

#     # Ожидание результата через 45 секунд
#     result = WebDriverWait(browser, 50).until(
#         EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
#     )

#     # Проверка результата
#     display_value = browser.find_element(By.CSS_SELECTOR, '.screen').text
#     assert display_value == '15', f"Expected result '15', but got '{display_value}'"


# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def test_calculator():
#     # Запуск браузера (например, Chrome).
#     driver = webdriver.Firefox()  # Убедитесь, что chromedriver в PATH

#     try:
#         # Открываем страницу калькулятора.
#         driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

#         # Вводим значение в поле с локатором #delay.
#         delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
#         delay_input.clear()
#         delay_input.send_keys("45")

#         # Нажимаем кнопки 7, +, 8 и =.
#         driver.find_element(By.CSS_SELECTOR, "btn.btn-outline-primary[7]").click()
#         driver.find_element(By.CSS_SELECTOR, "btn.btn-outline-primary[+]").click()
#         driver.find_element(By.CSS_SELECTOR, "btn.btn-outline-primary[8]").click()
#         driver.find_element(By.CSS_SELECTOR, "btn.btn-outline-primary[=]").click()

#         # Ждем 45 секунд (как указано в тесте).
#         time.sleep(45)

#         # Проверяем, что результат отображается правильно.
#         result_display = driver.find_element(By.CSS_SELECTOR, "#result")
#         assert result_display.text == "15", f"Ожидался результат '15', но получен '{result_display.text}'"

#     finally:
#         # Закрываем браузер.
#         driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_calculator(driver):
    # Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Вводим значение 45 в поле с локатором #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")

    # Нажимаем на кнопки 7, +, 8, =
    driver.find_element(By.CSS_SELECTOR, "btn#7").click()
    driver.find_element(By.CSS_SELECTOR, "btn#+").click()
    driver.find_element(By.CSS_SELECTOR, "btn#8").click()
    driver.find_element(By.CSS_SELECTOR, "btn#=").click()

    # Ждем, пока в окне отобразится результат 15
    wait = WebDriverWait(driver, 60)
    result = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#display"), "15"))
    assert result