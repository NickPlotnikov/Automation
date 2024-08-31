import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from FormReg_page import RegistrationPage
import allure

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест регистрации")
@allure.description("Проверка формы регистрации с различными данными.")
@allure.feature("Регистрация")
@allure.severity(allure.severity_level.CRITICAL)
def test_registration(driver):
    registration_page = RegistrationPage(driver)
    
    with allure.step("Заполнение формы регистрации"):
        registration_page.fill_form(
            first_name="Николай",
            last_name="Плотников",
            address="Краснодар, 3-77",
            email="test@skypro.com",
            phone="+79108737214",
            zip_code="",
            city="Краснодар",
            country="Россия",
            job_position="QA",
            company="SkyPro"
        )

    with allure.step("Отправка формы"):
        submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        driver.execute_script("arguments[0].click();", submit_button)

    with allure.step("Проверка цвета предупреждений"):
        check_color_by_class(registration_page, "alert-danger", '#842029')
        check_color_by_class(registration_page, "alert-success", '#0f5132')

@allure.step("Проверка цвета элемента")
def check_color_by_class(page, class_name, expected_color):
    field = page.get_element_by_class(class_name)
    actual_color = Color.from_string(field.value_of_css_property('color')).hex
    print(f"Expected color {expected_color}, but got {actual_color}")
    assert actual_color == expected_color