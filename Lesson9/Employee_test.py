from EmployeeApi import EmployeeApi
from EmployeeSQL import EmployeeSQL

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeSQL("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_employees():
    # Step 1: Create a company
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    # Step 2: Get employees from company via API
    api_employees = api.get_employee(company_id)

    # Step 3: Get employees from company via Database
    db_employees = db.get_employees(company_id)

    # Step 4: Verify that the employee lists are the same
    assert len(api_employees) == len(db_employees), "Employee counts should be equal"

def test_add_employee():
    # Step 1: Create a company
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    # Step 2: Get initial employee count via API
    initial_employees = api.get_employee(company_id)
    initial_count = len(initial_employees)

    # Step 3: Create an employee
    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    new_employee = api.create_employee(**employee_details)
    employee_id = new_employee["id"]

    # Step 4: Verify employee count increased by 1
    updated_employees = api.get_employee(company_id)
    assert len(updated_employees) == initial_count + 1, "Employee count should have increased by 1"

    # Step 5: Verify new employee details
    new_employee_record = next(emp for emp in updated_employees if emp["id"] == employee_id)
    assert all(new_employee_record[key] == value for key, value in employee_details.items()), "Employee details should match"

    # Clean-up: Delete new employee
    db.delete(employee_id)

def test_get_single_employee():
    # Step 1: Create a company and an employee
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    db.create(**employee_details)
    employee_id = db.get_max_id()

    # Step 2: Retrieve employee by ID via API
    employee = api.employee_id(employee_id)

    # Step 3: Assert employee details
    assert all(employee[key] == value for key, value in employee_details.items()), "Employee details should match"

    # Clean-up: Delete employee
    db.delete(employee_id)

def test_edit_employee():
    # Step 1: Create a company and an employee
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    db.create(**employee_details)
    employee_id = db.get_max_id()

    # Step 2: Update employee email
    new_email = "Pugachiha777@live.com"
    updated_employee = api.employee_change(employee_id, new_email=new_email)

    # Step 3: Assert changes
    assert updated_employee["id"] == employee_id, "Employee ID should match"
    assert updated_employee["email"] == new_email, "Employee email should be updated"

    # Clean-up: Delete employee
    db.delete(employee_id)
