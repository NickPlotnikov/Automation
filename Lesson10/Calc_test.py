from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from Calc_page import CalculatorPage
import pytest
import allure

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора с задержкой.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    
    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    with allure.step("Ввод значения задержки"):
        calculator_page.enter_delay_value("45")
    
    with allure.step("Ввод первого числа"):
        calculator_page.click_button("7")
    
    with allure.step("Выбор оператора"):
        calculator_page.click_operator_button("+")
    
    with allure.step("Ввод второго числа"):
        calculator_page.click_button("8")
    
    with allure.step("Нажатие кнопки равно"):
        calculator_page.click_equals_button()
    
    with allure.step("Получение и проверка результата"):
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
        result = result_element.text.strip()
        assert result == "15"
