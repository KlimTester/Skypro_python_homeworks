import requests
import allure


class EmployeeApi:
    allure.step("api. Инициализация")

    def __init__(self, url: str):
        self.url = url

    allure.step("api. Получить токен авторизации")

    def get_token(self, user='flora', password='nature-fairy') -> dict:
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    allure.step("api. Добавить компанию")

    def create_company(self, name: str, description="") -> dict:
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()

    allure.step("api. Получить список сотрудников по id компании")

    def get_employee(self, id: str) -> dict:
        resp = requests.get(self.url + '/employee?company=' + id)
        return resp.json()

    allure.step("api. Добавить сотрудника")

    def create_employee(self, first_name: str, last_name: str, middle_name: str, id_company: int, email: str, url: str, phone: str) -> dict:
        employee = {
             "firstName": first_name,
             "lastName": last_name,
             "middleName": middle_name,
             "companyId": id_company,
             "email": email,
             "url": url,
             "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=my_headers)
        return resp.json()

    allure.step("api. Получить сотрудника по id")

    def employee_id(self, id: str) -> dict:
        resp = requests.get(self.url + '/employee/' + id)
        return resp.json()

    allure.step("api. Изменить информацию о сотруднике")

    def employee_change(self, id: str, last_name="", email="", url="", phone="") -> dict:
        employee = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + id,
                              json=employee, headers=my_headers)
        return resp.json()