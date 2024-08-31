import requests

class Company:
    def __init__(self, url: str) -> None:
        """
        Инициализация класса Company.

        :param url: Базовый URL для API компании.
        """
        self.url = url

    def get_id_company(self) -> int:
        """
        Получает ID компании.

        :return: ID последней компании.
        """
        id_company = requests.get(self.url + '/company')
        return id_company.json()[-1]['id']
