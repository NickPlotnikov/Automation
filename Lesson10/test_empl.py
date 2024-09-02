from empl_api import ApiEmpl
from company import Company
from empl_db import DbEmployee
import allure

db = DbEmployee("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
company = Company("https://x-clients-be.onrender.com")
param_id = "?company=" + str(company.get_id_company())
company_id = company.get_id_company()
api = ApiEmpl("https://x-clients-be.onrender.com")

body = {
    "id": 1010108711,
    "firstName": "string",
    "lastName": "string",
    "middleName": "string",
    "companyId": company_id,
    "email": "string@bl.yu",
    "url": "string",
    "phone": "string",
    "birthdate": "2023-08-14T11:02:45.622Z",
    "isActive": "true"
}

@allure.title("Получение списка сотрудников")
@allure.description("Тест проверяет получение списка сотрудников компании.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_get_list_employee2():
    with allure.step("Получение списка сотрудников через API"):
        api_result = api.get_list_employee2(param_id).json()
    with allure.step("Получение списка сотрудников из базы данных"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Сравнение количества сотрудников"):
        assert len(api_result) == len(db_result)

@allure.title("Добавление нового сотрудника")
@allure.description("Тест проверяет добавление нового сотрудника в компанию.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_employee2():
    with allure.step("Получение текущего списка сотрудников из базы данных"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Добавление нового сотрудника через API"):
        api.add_new_employee2(body)
    with allure.step("Получение обновленного списка сотрудников через API"):
        api_response = api.get_list_employee2(param_id).json()
    with allure.step("Проверка увеличения количества сотрудников"):
        assert len(api_response) - len(db_result) == 1

@allure.title("Получение нового сотрудника")
@allure.description("Тест проверяет получение нового сотрудника по ID.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.NORMAL)
def test_get_new_employee2():
    with allure.step("Получение ID нового сотрудника через API"):
        api_new_employee = api.get_list_employee2(param_id).json()[-1]['id']
    with allure.step("Получение ID нового сотрудника из базы данных"):
        db_new_employee = db.get_id_new_employee()
    with allure.step("Сравнение ID сотрудника"):
        assert api_new_employee == db_new_employee

@allure.title("Создание сотрудника в базе данных")
@allure.description("Тест проверяет создание сотрудника в базе данных и получение его через API.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_employee():
    with allure.step("Добавление нового сотрудника в базу данных"):
        db.add_new_employee("Николай", "Плотников", "89180462317", True, company_id)
    with allure.step("Получение данных сотрудника через API"):
        data_employee = api.get_new_employee2(db.get_id_new_employee()).json()
    with allure.step("Проверка данных сотрудника"):
        assert data_employee["firstName"] == "Николай"
        assert data_employee["lastName"] == "Плотников"
        assert data_employee["phone"] == "89180462317"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    with allure.step("Удаление сотрудника из базы данных"):
        db.delete(db.get_id_new_employee())

@allure.title("Редактирование сотрудника")
@allure.description("Тест проверяет редактирование данных сотрудника в базе данных.")
@allure.feature("Сотрудники")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_employee():
    with allure.step("Добавление нового сотрудника в базу данных"):
        db.add_new_employee("Николай", "Плотников", "89180462317", True, company_id)
    id = db.get_id_new_employee()
    with allure.step("Редактирование данных сотрудника в базе данных"):
        db.edit_employee("Эдди", "Мерфин", "89180463434", True, company_id, id)
    with allure.step("Получение данных сотрудника через API"):
        data_employee = api.get_new_employee2(id).json()
    with allure.step("Проверка обновленных данных сотрудника"):
        assert data_employee["firstName"] == "Эдди"
        assert data_employee["lastName"] == "Мерфин"
        assert data_employee["phone"] == "89180463434"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    with allure.step("Удаление сотрудника из базы данных"):
        db.delete(id)
