from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_screen():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    waiter = WebDriverWait(driver, 50)

    # Поиск элементов и присваивание к переменным.
    delay = driver.find_element(By.CSS_SELECTOR, '#delay')

    # Действия с формами
    delay.clear()
    delay.send_keys('45')

    # Поиск ссылки элемента позиции магазина и клик по ссылке
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    # Еще один поиск ссылки элемента позиции магазина  
    screen = driver.find_element(By.CSS_SELECTOR, 'div.screen')
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
    assert screen.text == "15"

    driver.quit()


test_screen()