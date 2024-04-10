from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def wait_of_element_located(css, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, css)
        )
    )
    return element


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

# Поиск элементов и присваивание к переменным.
first_name = wait_of_element_located(css='[name="first-name"]', driver=driver)
last_name = wait_of_element_located(css='[name="last-name"]', driver=driver)
address = wait_of_element_located(css='[name="address"]', driver=driver)
zip_code = wait_of_element_located(css='[name="zip-code"]', driver=driver)
city = wait_of_element_located(css='[name="city"]', driver=driver)
country = wait_of_element_located(css='[name="country"]', driver=driver)
e_mail = wait_of_element_located(css='[name="e-mail"]', driver=driver)
phone = wait_of_element_located(css='[name="phone"]', driver=driver)
job_position = wait_of_element_located(css='[name="job-position"]', driver=driver)
company = wait_of_element_located(css='[name="company"]', driver=driver)

# Действия с формами
first_name.send_keys('Иван')
last_name.send_keys('Петров')
address.send_keys('Ленина, 55-3')
zip_code.send_keys()
city.send_keys('Москва')
country.send_keys('Россия')
e_mail.send_keys('test@skypro.com')
phone.send_keys('+7985899998787')
job_position.send_keys('QA')
company.send_keys('SkyPro')

# Поиск ссылки элемента позиции магазина и клик по ссылке
wait_of_element_located(css='[type="submit"]', driver=driver).click()

# Еще один поиск ссылки элемента позиции магазина


def test_alert_danger():
    zip_code_color = wait_of_element_located(css='#zip-code', driver=driver).value_of_css_property("background-color")
    assert zip_code_color == "rgba(248, 215, 218, 1)"


test_alert_danger()

# Еще один поиск ссылки элемента позиции магазина


def test_alert_success():
    allert_success = driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
    for form in allert_success:
        assert form.value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"


test_alert_success()