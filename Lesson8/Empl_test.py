from Empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "NickPlotnikov", "B")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "NickPlotnikov"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "B"


def test_get_employee_by_id():
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "NickPlotnikov", "Be")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "NickPlotnikov"
    assert get_info["lastName"] == "Be"

def test_get_list_employee_without_company_id(): # Тестирование получения списка сотрудников без companyId:
    try:
        api.get_list_employee(None)
    except Exception as e:
        assert str(e) == "Company ID is required"

def test_get_employee_by_id_without_id(): # Тестирование получения сотрудника без id:
    try:
        api.get_employee_by_id(None)
    except Exception as e:
        assert str(e) == "Employee ID is required"

def test_add_employee_without_request_body(): # Тестирование создания сотрудника без тела запроса:
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    
    try:
        api.add_new_employee(new_id, None, None)
    except Exception as e:
        assert str(e) == "Request body cannot be empty"

def test_add_employee_without_token(): # Тестирование создания сотрудника без токена:
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    
    try:
        api.add_new_employee(new_id, "NickPlotnikov", "B", token=None)
    except Exception as e:
        assert str(e) == "Token is required"

def test_change_employee_info():
    name = "Nick"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "NickPlotnikov", "Ber")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Ber2", "test2@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test2@mail.ru"
    assert update["isActive"] == True