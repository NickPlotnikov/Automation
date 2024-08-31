from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine import ResultProxy

class DbEmployee:
    scripts = {
        "list_employee": text("select * from employee where company_id =:company_id"),
        "new_employee": text("insert into employee (first_name, last_name, phone, is_active, company_id) values (:first_name, :last_name, :phone, :is_active, :company_id)"),
        "id_new_employee": text("select id from employee where company_id = (select max(\"company_id\") from employee) and id = (select max(\"id\") from employee)"),
        "delete": text("delete from employee where id =:new_id"),
        "edit": text("update employee set first_name =:first_name, last_name =:last_name, phone =:phone, is_active =:is_active where id =:id")
    }

    def __init__(self, connection_string: str):
        """
        Инициализация подключения к базе данных.

        :param connection_string: Строка подключения к базе данных.
        """
        self.__db = create_engine(connection_string)

    def get_list_employee(self, company_id: int) -> list:
        """
        Получает список сотрудников компании из базы данных.

        :param company_id: ID компании.
        :return: Список сотрудников.
        """
        list_employee = self.__db.execute(self.scripts['list_employee'], company_id=company_id)
        employees = list_employee.fetchall()
        return employees

    def get_id_new_employee(self) -> int:
        """
        Получает ID нового сотрудника.

        :return: ID сотрудника.
        """
        new_employee = self.__db.execute(self.scripts['id_new_employee'])
        db_new_employee = new_employee.fetchone()[0]
        return db_new_employee

    def add_new_employee(self, first_name: str, last_name: str, phone: str, is_active: bool, company_id: int) -> None:
        """
        Добавляет нового сотрудника в базу данных.

        :param first_name: Имя сотрудника.
        :param last_name: Фамилия сотрудника.
        :param phone: Телефон сотрудника.
        :param is_active: Активность сотрудника.
        :param company_id: ID компании.
        """
        self.__db.execute(self.scripts['new_employee'], first_name=first_name, last_name=last_name, phone=phone, is_active=is_active, company_id=company_id)

    def edit_employee(self, first_name: str, last_name: str, phone: str, is_active: bool, company_id: int, id: int) -> None:
        """
        Изменяет данные сотрудника в базе данных.

        :param first_name: Имя сотрудника.
        :param last_name: Фамилия сотрудника.
        :param phone: Телефон сотрудника.
        :param is_active: Активность сотрудника.
        :param company_id: ID компании.
        :param id: ID сотрудника.
        """
        self.__db.execute(self.scripts['edit'], first_name=first_name, last_name=last_name, phone=phone, is_active=is_active, company_id=company_id, id=id)

    def delete(self, id: int) -> None:
        """
        Удаляет сотрудника из базы данных.

        :param id: ID сотрудника.
        """
        self.__db.execute(self.scripts['delete'], new_id=id)
