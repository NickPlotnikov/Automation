import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def open_labirint(driver):
    driver.get("https://www.labirint.ru/")

def search_books(driver, query):
    search_box = driver.find_element(By.ID, "search-field")
    search_box.send_keys(query)
    search_box.submit()

def add_all_books_to_cart(driver):
    # Ожидание появления результатов поиска
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
    )
    
    # Найти все кнопки "В корзину" и добавить все книги
    add_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'В корзину')]")
    for button in add_buttons:
        button.click()
        time.sleep(1)  # Задержка, чтобы избежать блокировки сайта

def go_to_cart(driver):
    cart_button = driver.find_element(By.XPATH, "//a[@href='/cart/']")
    cart_button.click()

def check_cart_item_count(driver, expected_count):
    # Ожидание загрузки страницы корзины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "total-count"))
    )
    
    # Получить количество товаров в корзине
    cart_count = int(driver.find_element(By.CLASS_NAME, "total-count").text)
    assert cart_count == expected_count, f"Ожидалось {expected_count} товаров, но найдено {cart_count}"

def main():
    driver = webdriver.Chrome()

    try:
        open_labirint(driver)
        search_books(driver, "Python")
        
        # Найти и добавить все книги в корзину
        add_all_books_to_cart(driver)
        
        # Перейти в корзину
        go_to_cart(driver)
        
        # Проверить количество товаров в корзине
        check_cart_item_count(driver, len(driver.find_elements(By.XPATH, "//a[contains(text(),'В корзину')]")))

    finally:
        driver.quit()

if __name__ == "__main__":
    main()