from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера Gecko
driver = webdriver.Firefox()

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Клик по синей кнопке
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

# Задержка для наглядности
time.sleep(2)

# Закрытие браузера
driver.quit()
