from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора с заданным веб-драйвером.

        :param driver: Объект веб-драйвера для управления браузером.
        """
        self.driver = driver

    def open_page(self, url: str) -> None:
        """
        Открывает указанную веб-страницу.

        :param url: URL страницы для открытия.
        :return: None
        """
        self.driver.get(url)

    def enter_delay_value(self, delay_value: str) -> None:
        """
        Вводит значение задержки в поле ввода.

        :param delay_value: Значение задержки для ввода.
        :return: None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку с заданным текстом.

        :param button_text: Текст кнопки для нажатия.
        :return: None
        """
        button_locator = f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    def click_operator_button(self, operator: str) -> None:
        """
        Нажимает на кнопку оператора с заданным текстом.

        :param operator: Текст оператора для нажатия.
        :return: None
        """
        operator_locator = f"//span[contains(@class, 'operator') and text()='{operator}']"
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    def click_equals_button(self) -> None:
        """
        Нажимает на кнопку равенства.

        :return: None
        """
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    def get_result_text(self) -> str:
        """
        Получает текст результата из экрана калькулятора.

        :return: Текст результата.
        """
        result_element = WebDriverWait(self.driver, 46).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
        )
        return result_element.text
