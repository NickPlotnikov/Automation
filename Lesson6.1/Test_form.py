# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture(scope="module")
# def browser():
#     # Инициализация драйвера Firefox
#     driver = webdriver.Firefox()
#     yield driver
#     driver.quit()

# def test_form_submission(browser):
#     # Открытие страницы формы
#     browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

#     # Заполнение формы
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[1]/div[1]/label/input").send_keys('Иван')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[1]/div[2]/label/input").send_keys('Петров')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[1]/label/input").send_keys('Ленина, 55-3')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[3]/div[1]/label/input").send_keys('test@skypro.com')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[3]/div[2]/label/input").send_keys('+7985899998787')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[2]/label/input").clear()  # Оставить пустым
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[3]/label/input").send_keys('Москва')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[2]/div[4]/label/input").send_keys('Россия')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[4]/div[1]/label/input").send_keys('QA')
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[4]/div[2]/label/input").send_keys('SkyPro')

#     # Нажатие на кнопку Submit
#     browser.find_element(By.XPATH, "/html/body/main/div/form/div[5]/div/button").click()

#     # Ожидание реакции на отправку формы
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@name='zip', "zip-code"]"))
#     )

#     # Проверка, что поле Zip code подсвечено красным
#     zip_code_field = browser.find_element(By.XPATH, "//input[@name='zip']")
#     assert 'is-invalid' in zip_code_field.get_attribute('class'), "Zip code field is not highlighted red."

#     # Проверка, что остальные поля подсвечены зеленым
#     fields_to_check = [
#         "//input[@name='first-name']",
#         "//input[@name='last-name']",
#         "//input[@name='address']",
#         "//input[@name='email']",
#         "//input[@name='phone']",
#         "//input[@name='city']",
#         "//select[@name='country']",
#         "//input[@name='job-position']",
#         "//input[@name='company']"
#     ]

#     for field_xpath in fields_to_check:
#         field = browser.find_element(By.XPATH, field_xpath)
#         assert 'is-valid' in field.get_attribute('class'), f"Field {field_xpath} is not highlighted green."


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    # Запуск браузера Firefox
    driver = webdriver.Firefox()  # Убедитесь, что geckodriver в PATH

    try:
        # Открываем страницу формы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполняем форму
        driver.find_element(By.NAME, "first_name").send_keys("Иван")
        driver.find_element(By.NAME, "last_name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "zip").send_keys("")  # Оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ожидаем, когда форма будет обработана
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='zip']"))
        )

        # Проверка, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.NAME, "zip")
        assert "red" in zip_code_field.get_attribute("style"), "Поле Zip code должно подсвечиваться красным."

        # Проверка, что остальные поля подсвечены зеленым
        fields = ["first_name", "last_name", "address", "email", "phone", "city", "country", "job", "company"]
        for field in fields:
            input_field = driver.find_element(By.NAME, field)
            assert "green" in input_field.get_attribute("style"), f"Поле {field} должно подсвечиваться зеленым."

    finally:
        # Закрываем браузер
        driver.quit()
        