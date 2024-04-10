from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def wait_of_element_located(css, driver):
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, css)
        )
    )
    return element

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')

# Поиск элементов и присваивание к переменным.
username = wait_of_element_located(css='#user-name', driver=driver)
password = wait_of_element_located(css='#password', driver=driver)

# Действия с формами
username.send_keys('standard_user')
password.send_keys('secret_sauce')


# Поиск ссылки элемента позиции магазина и клик по ссылке
wait_of_element_located(css='#login-button', driver=driver).click()
wait_of_element_located(css='#add-to-cart-sauce-labs-backpack', driver=driver).click()
wait_of_element_located(css='#add-to-cart-sauce-labs-bolt-t-shirt', driver=driver).click()
wait_of_element_located(css='#add-to-cart-sauce-labs-onesie', driver=driver).click()
wait_of_element_located(css='a.shopping_cart_link', driver=driver).click()
wait_of_element_located(css='#checkout', driver=driver).click()
# Еще один поиск ссылки элемента позиции магазина
first_name = wait_of_element_located(css='#first-name', driver=driver)
last_name = wait_of_element_located(css='#last-name', driver=driver)
postal_code = wait_of_element_located(css='#postal-code', driver=driver)

first_name.send_keys('Ilia')
last_name.send_keys('Klimov')
postal_code.send_keys('2403CW')

wait_of_element_located(css='#continue', driver=driver).click()


def test_total():
    total = wait_of_element_located(css='div.summary_total_label', driver=driver)
    assert total.text == 'Total: $58.29'


test_total()