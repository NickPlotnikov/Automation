from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver = webdriver.Chrome()

try:
    # Откройте страницу
    driver.get('http://the-internet.herokuapp.com/inputs')

    # Явное ожидание, чтобы поле ввода стало доступным
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

    # Введите текст 1000 в поле
    input_field.send_keys('1000', Keys.RETURN)
    print("Введен текст '1000'.")
    sleep(5)
    # Очистите поле
    input_field.clear()
    print("Поле очищено.")

    # Введите текст 999 в поле
    input_field.send_keys('999', Keys.RETURN)
    print("Введен текст '999'.")
    sleep(5)
finally:
    # Закрыть браузер после выполнения
    driver.quit()
sleep(5)