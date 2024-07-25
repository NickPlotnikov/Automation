from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки браузера Firefox
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# Запуск Firefox через Selenium
service = Service()

def run_script():
    driver = webdriver.Firefox(service=service, options=options)
    try:
        # Откройте страницу
        driver.get('http://uitestingplayground.com/dynamicid')

        # Явное ожидание, чтобы кнопка стала доступной
        wait = WebDriverWait(driver, 10)
        blue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class*="btn-primary"]')))

        # Кликните на синюю кнопку
        blue_button.click()
        print("Клик по синей кнопке выполнен.")
        
        # Ждем несколько секунд, чтобы убедиться, что действие завершилось
        time.sleep(2)
    
    finally:
        # Закрыть браузер после выполнения
        driver.quit()

# Запуск скрипта три раза подряд
for i in range(3):
    print(f"Запуск {i+1}")
    run_script()
    time.sleep(1)