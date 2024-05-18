from sqlalchemy import create_engine
from sqlalchemy import text
import allure


class EmployeeSQL:
    __scripts = {
        "select by id_company": text("select * from employee where company_id = :company_id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee(\"first_name\", \"last_name\", \"middle_name\", \"company_id\", \"email\", \"phone\") values (:first_name, :last_name, :middle_name, :company_id, :email, :phone)"),
        "get max id": text("select MAX(\"id\") from employee")
    }

    allure.step("БД. Подключение к БД")

    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string).connect()

    allure.step("БД. Получить сотрудников по id компании")

    def get_employees(self, my_params: str) -> bool:
        return self.__db.execute(self.__scripts["select by id_company"], {"company_id": my_params}).fetchall()

    allure.step("БД. Удалить сотрудника по id")

    def delete(self, id: int):
        self.__db.execute(self.__scripts["delete by id"], {"id_to_delete": id})

    allure.step("БД. Создать сотрудника")

    def create(self, first_name: str, last_name: str, middle_name: str, company_id: int, email: str, phone: str):
        self.__db.execute(self.__scripts["insert new"], {"first_name": first_name,
                                                         "last_name": last_name,
                                                         "middle_name": middle_name,
                                                         "company_id": company_id,
                                                         "email": email,
                                                         "phone": phone
                                                         })
        self.__db.commit()

    allure.step("БД. Получить максимальный id организации")

    def get_max_id(self) -> bool:
        return self.__db.execute(self.__scripts["get max id"]).\
               fetchall()[0][0]