from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# Шаг 1: Открываем страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Шаг 2: Кликаем 5 раз на кнопку Add Element
add_element_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_element_button.click()

# Даем время для загрузки элементов (не всегда необходимо, но может помочь)
time.sleep(5)

# Шаг 3: Собираем список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Шаг 4: Выводим размер списка
print(f"Количество кнопок Delete: {len(delete_buttons)}")

# Закрываем браузер
driver.quit()