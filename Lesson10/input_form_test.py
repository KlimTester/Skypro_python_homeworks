from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.InputFormPage import InputFormPage
import allure


@allure.title("Заполнение формы")
@allure.description("Проверка подсвеченности обязательных полей")
@allure.feature("READ")
@allure.severity("blocker")
def test_unput_form():
    with allure.step("Открываем браузер"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        
    with allure.step("Открытие страницы: https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
        input_form = InputFormPage(browser)
    
    with allure.step("Ввод в поле First Name"):
        input_form.first_name('Иван')
    
    with allure.step("Ввод в поле Last Name"):
        input_form.last_name('Петров')

    with allure.step("Ввод в поле Address"):
        input_form.address('Ленина, 55-3')

    with allure.step("Ввод в поле email"):
        input_form.e_mail('test@skypro.com')

    with allure.step("Ввод в поле Phone"):
        input_form.phone('+7985899998787')

    with allure.step("Ввод в поле Zip Code"):
        input_form.zip_code('')

    with allure.step("Ввод в поле City"):
        input_form.city('Москва')

    with allure.step("Ввод в поле Country"):
        input_form.country('Россия')
    
    with allure.step("Ввод в поле Job position"):
        input_form.job_position('QA')
    
    with allure.step("Ввод в поле Company"):
        input_form.company('SkyPro')
    
    with allure.step("Нажатие кнопки Submit"):
        input_form.submit()

    with allure.step("Проверка подсвеченности цветом поля Zip code"):
        alert_danger = input_form.alert_danger()

        assert alert_danger == "rgba(248, 215, 218, 1)"

    with allure.step("Проверка подсвеченности цветом заполненных полей"):
        alert_succes = input_form.alert_success()

        assert alert_succes == "rgba(209, 231, 221, 1)"

    with allure.step("Закрытие браузера"):
        browser.quit()