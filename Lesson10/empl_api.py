import requests

class ApiEmpl:
    def __init__(self, url: str) -> None:
        """
        Инициализация API для работы с сотрудниками.

        :param url: Базовый URL для API сотрудников.
        """
        self.url = url

    def auth2(self, login: str = "leonardo", password: str = "leads") -> str:
        """
        Авторизация пользователя.

        :param login: Логин пользователя.
        :param password: Пароль пользователя.
        :return: Токен пользователя.
        """
        body = {
            "username": login,
            "password": password
        }
        response = requests.post(self.url + '/auth/login', json=body)
        return response.json()["userToken"]

    def get_list_employee2(self, params: str = None) -> requests.Response:
        """
        Получает список сотрудников компании.

        :param params: Параметры запроса.
        :return: Ответ API.
        """
        response = requests.get(self.url + '/employee' + params)
        return response

    def add_new_employee2(self, body: dict) -> requests.Response:
        """
        Добавляет нового сотрудника.

        :param body: Данные нового сотрудника.
        :return: Ответ API.
        """
        headers = {'x-client-token': self.auth2()}
        response = requests.post(self.url + '/employee/', headers=headers, json=body)
        return response

    def get_new_employee2(self, id: int) -> requests.Response:
        """
        Получает сотрудника по ID.

        :param id: ID сотрудника.
        :return: Ответ API.
        """
        response = requests.get(self.url + '/employee/' + str(id))
        return response

    def change_new_employee2(self, id: int, new_body: dict) -> requests.Response:
        """
        Изменяет данные о сотруднике.

        :param id: ID сотрудника.
        :param new_body: Новые данные сотрудника.
        :return: Ответ API.
        """
        headers = {'x-client-token': self.auth2()}
        response = requests.patch(self.url + '/employee/' + str(id), headers=headers, json=new_body)
        return response
