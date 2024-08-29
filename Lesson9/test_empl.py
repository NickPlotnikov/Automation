from empl_api import ApiEmpl
from company import Company
from empl_db import DbEmployee

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


def test_get_list_employee2():
    api_result = api.get_list_employee2(param_id)
    api_result = api_result.json()
    db_result = db.get_list_employee(company_id)
    assert len(api_result) == len(db_result)


def test_add_employee2():
    db_result = db.get_list_employee(company_id)
    api.add_new_employee2(body)
    api_response = api.get_list_employee2(param_id)
    api_response = api_response.json()
    assert len(api_response)-len(db_result) == 1


def test_get_new_employee2():
    resp = api.get_list_employee2(param_id)
    api_new_employee = resp.json()[-1]['id']
    db_new_employee = db.get_id_new_employee()
    assert api_new_employee == db_new_employee


def test_create_employee():
    db_result = db.get_list_employee(company_id)
    db.add_new_employee("Николай", "Плотников", "89180462317", True, company_id)
    data_employee = api.get_new_employee2(db.get_id_new_employee())
    data_employee = data_employee.json()
    assert data_employee["firstName"] == "Николай"
    assert data_employee["lastName"] == "Плотников"
    assert data_employee["phone"] == "89180462317"
    assert data_employee["isActive"] == True
    assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)



def test_edit_employee():
    db.add_new_employee("Николай", "Плотников", "89180462317", True, company_id)
    id = db.get_id_new_employee()
    db.edit_employee("Эдди", "Мерфин", "89180463434", True, company_id, id)
    data_employee = api.get_new_employee2(id)
    data_employee = data_employee.json()
    assert data_employee["firstName"] == "Эдди"
    assert data_employee["lastName"] == "Мерфин"
    assert data_employee["phone"] == "89180463434"
    assert data_employee["isActive"] == True
    assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)