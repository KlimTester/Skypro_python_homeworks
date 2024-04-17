# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

from Pages.FillingTheFormPage import FillingTheFormPage


def test_unput_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    input_form = FillingTheFormPage(browser)
    input_form.input_form_first_name('Иван')
    input_form.input_form_last_name('Петров')
    input_form.input_form_address('Ленина, 55-3')
    input_form.input_form_e_mail('test@skypro.com')
    input_form.input_form_phone('+7985899998787')
    input_form.input_form_zip_code('')
    input_form.input_form_city('Москва')
    input_form.input_form_country('Россия')
    input_form.input_form_job_position('QA')
    input_form.input_form_company('SkyPro')

    alert_danger = input_form.alert_danger()

    assert alert_danger == "rgba(248, 215, 218, 1)"

    alert_succes = input_form.alert_success()

    assert alert_succes == "rgba(209, 231, 221, 1)"

    browser.quit()