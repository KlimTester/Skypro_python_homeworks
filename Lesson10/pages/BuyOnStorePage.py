from selenium.webdriver.common.by import By
import allure


class BuyOnStorePage():
    allure.step("Открытие сайта магазина: https://www.saucedemo.com/")

    def __init__(self, driver: str):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    allure.step("Ввод в поле Username")

    def authorization_username(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)

    allure.step("Ввод в поле Password и клик по кнопке Login")

    def authorization_password(self, term: str): 
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    allure.step("Добавление в корзину товаров")

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    allure.step("Переход в корзину")

    def shopping_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    allure.step("Нажатие Checkout")

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    allure.step("Ввод в поле First Name")

    def input_first_name(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(term)

    allure.step("Ввод в поле Last Name")

    def input_last_name(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(term)

    allure.step("Ввод в поле Zip/Postal Code")

    def input_postal_code(self, term: str):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(term)

    allure.step("Нажатие Continue")

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    allure.step("Отображение со страницы Итоговой стоимости (Total)")

    def summary_total(self) -> str:
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total