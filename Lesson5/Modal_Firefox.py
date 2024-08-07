from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки браузера Firefox
options = Options()
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# Запуск Firefox через Selenium
service = Service()
driver = webdriver.Firefox()

try:
    # Откройте страницу
    driver.get('http://the-internet.herokuapp.com/entry_ad')

    # Явное ожидание, чтобы модальное окно стало видимым
    wait = WebDriverWait(driver, 10)
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal .modal-footer p')))

    # Нажмите на кнопку Close
    close_button.click()
    print("Модальное окно закрыто.")

finally:
    # Закрыть браузер после выполнения
    driver.quit()