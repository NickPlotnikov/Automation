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
    driver.get('http://uitestingplayground.com/ajax')

    # Нажать на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, 'button#ajaxButton')
    blue_button.click()

    # Ожидание, пока текст появится в зеленой плашке
    green_banner = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div#content'))
    )

    # Получение текста из зеленой плашки
    loaded_text = green_banner.text

    # Вывод текста в консоль
    print(loaded_text)

finally:
    # Закрытие браузера
    driver.quit() 
       
# Ожидание текста в зеленой плашке: Используется WebDriverWait для ожидания, пока элемент с текстом не станет видимым. Это обеспечивает корректную работу без использования sleep().
