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
    driver.get('http://uitestingplayground.com/textinput')

    # Указать в поле ввода текст "SkyPro"
    text_input = driver.find_element(By.ID, 'newButtonName')
    text_input.send_keys('SkyPro')

    # Нажать на синюю кнопку
    blue_button = driver.find_element(By.ID, 'updatingButton')
    blue_button.click()

    # Ожидание, пока текст кнопки изменится на "SkyPro"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro')
    )

    # Получение текста кнопки
    button_text = blue_button.text

    # Вывод текста в консоль
    print(button_text)

finally:
    # Закрытие браузера
    driver.quit()
    
# Ожидание изменения текста кнопки: Используется WebDriverWait для ожидания, пока текст кнопки не изменится на "SkyPro".