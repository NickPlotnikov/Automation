import pytest
from selenium import webdriver
from Mag_page import LoginPage, ProductsPage, CheckoutPage
import allure

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Полное завершение покупки")
@allure.description("Тест на полное завершение покупки в интернет-магазине.")
@allure.feature("Покупка")
@allure.severity(allure.severity_level.CRITICAL)
def test_complete_purchase(browser):
    Mag_page_url = "https://www.saucedemo.com/"

    # Шаг 1: Создание страниц
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = CheckoutPage(browser)

    with allure.step("Авторизация пользователя"):
        login_page.login_as_standard_user()

    with allure.step("Добавление товаров в корзину"):
        products_page.add_products_to_cart("Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")

    with allure.step("Переход в корзину"):
        products_page.go_to_shopping_cart()

    with allure.step("Оформление заказа"):
        checkout_page.proceed_to_checkout()

    # Шаг 6: Заполнение персональной информации
    # Предполагаем, что метод fill_personal_info существует в классе PersonalInfoPage
    personal_info_page.fill_personal_info("Andrey", "B", "123")

    with allure.step("Проверка итоговой стоимости и завершение покупки"):
        total_amount = overview_page.get_total_amount()
        assert total_amount == "58.29", f"Expected '58.29', but got {total_amount}"
        overview_page.complete_purchase()
