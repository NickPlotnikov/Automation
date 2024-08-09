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
driver = webdriver.Firefox(service=service, options=options)

try:
    # Перейти на страницу
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    # Получение значения атрибута src у 3-й картинки
    third_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[4]"))
    )
    third_image_src = third_image.get_attribute('src')

    # Вывод значения в консоль
    print(third_image_src)

finally:
    # Закрытие браузера
    driver.quit()