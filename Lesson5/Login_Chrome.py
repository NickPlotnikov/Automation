from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки браузера Chrome
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# Запуск Chrome через Selenium
service = Service()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Откройте страницу
    driver.get('http://the-internet.herokuapp.com/login')

    # Найдите поле ввода username и введите значение
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('tomsmith')

    # Найдите поле ввода password и введите значение
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('SuperSecretPassword!')

    # Найдите и нажмите кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Явное ожидание для проверки успешного входа (можно добавить дополнительные проверки здесь)
    WebDriverWait(driver, 10).until(EC.url_contains('secure'))

    print("Успешная авторизация!")

finally:
    # Закрыть браузер после выполнения
    driver.quit()