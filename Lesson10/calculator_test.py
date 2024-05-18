from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage
import allure


@allure.title("Проверка калькулятора")
@allure.description("Результат должен отобразиться через 45 секунд")
@allure.feature("FUNCTIONALITY")
@allure.severity("blocker")
def test_calculator():
    with allure.step("Открываем браузер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Открытие страницы: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
        calculator = CalculatorPage(browser)

    with allure.step("Ввод в поле значение 45"):
        calculator.delay('45')

    with allure.step("Нажимаем на кнопки 7+8="):
        calculator.click('7')
        calculator.click('+')
        calculator.click('8')
        calculator.click('=')

    with allure.step("Ожидание результата после 45 секунд"):
        screen = calculator.screen("15")

    with allure.step("Проверка ответа"):
        assert screen == '15'

    with allure.step("Закрытие браузера"):
        browser.quit()