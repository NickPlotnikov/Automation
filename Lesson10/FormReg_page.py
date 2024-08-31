from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


class RegistrationPage:
    def __init__(self, driver):
        """
        Инициализирует страницу регистрации с заданным веб-драйвером.

        :param driver: Объект веб-драйвера для управления браузером.
        """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: str, 
                  zip_code: str, city: str, country: str, job_position: str, company: str) -> None:
        """
        Заполняет форму регистрации.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param address: Адрес.
        :param email: Электронная почта.
        :param phone: Телефон.
        :param zip_code: Почтовый индекс.
        :param city: Город.
        :param country: Страна.
        :param job_position: Должность.
        :param company: Компания.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)

    def get_element_by_class(self, class_name: str):
        """
        Получает элемент по имени класса.

        :param class_name: Имя класса элемента.
        :return: Найденный элемент.
        """
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return element

    def submit_form(self) -> None:
        """
        Отправляет форму регистрации.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()
