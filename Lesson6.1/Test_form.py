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


# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def test_form_submission():
#     # Запуск браузера Firefox
#     driver = webdriver.Firefox()  # Убедитесь, что geckodriver в PATH

#     try:
#         # Открываем страницу формы
#         driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

#         # Заполняем форму
#         driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Иван")
#         driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Петров")
#         driver.find_element(By.XPATH, "//input[@name='address']").send_keys("Ленина, 55-3")
#         driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@skypro.com")
#         driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("+7985899998787")
#         driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("")  # Оставляем пустым
#         driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Москва")
#         driver.find_element(By.XPATH, "//input[@name='country']").send_keys("Россия")
#         driver.find_element(By.XPATH, "//input[@name='job']").send_keys("QA")
#         driver.find_element(By.XPATH, "//input[@name='company']").send_keys("SkyPro")

#         # Нажимаем кнопку Submit
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()

#         # Ожидаем, когда форма будет обработана
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//input[@name='zip']"))
#         )

#         # Проверка, что поле Zip code подсвечено красным
#         zip_code_field = driver.find_element(By.XPATH, "//input[@name='zip']")
#         assert "red" in zip_code_field.get_attribute("style"), "Поле Zip code должно подсвечиваться красным."

#         # Проверка, что остальные поля подсвечены зеленым
#         fields = [
#             "first_name", "last_name", "address", "email", "phone",
#             "city", "country", "job", "company"
#         ]
        
#         for field in fields:
#             input_field = driver.find_element(By.XPATH, f"//input[@name='{field}']")
#             assert "green" in input_field.get_attribute("style"), f"Поле {field} должно подсвечиваться зеленым."

#     finally:
#         # Закрываем браузер
#         driver.quit()

      
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from time import sleep

@pytest.fixture(scope="module")
def browser():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window
    yield driver
    driver.quit()

def test_data_types_form(browser):
    # Открытие страницы формы
    browser.get(URL_1)
    form_data = {         
        'first-name': first_name,
        'last-name': last_name,
        'address': address,
        'e-mail': email,
        'phone': phone,
        'zip-code': zip_code,  # Оставить пустым
        'city': 'city',
        'country': country,
        'job-position': job_position,
        'company': company
    }
        
    # Ожидание реакции на отправку формы
    for field_name, value in form_data.items():
         browser.find_element(By.NAME, field_name).send_keys(value)
   
    # Ожидаем, когда форма будет обработана
    WebDriverWait(browser, 40, 0.1).until(
         EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(2)    

    # Проверка, что остальные поля подсвечены зеленым
    field_classes = {
            "zip-code": "danger",
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
           