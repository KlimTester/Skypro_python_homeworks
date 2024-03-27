from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера Gecko
driver = webdriver.Firefox()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "1000"
input_field.send_keys("1000")

# Задержка для наглядности
time.sleep(1)

# Очищаем поле ввода
input_field.clear()

# Задержка для наглядности
time.sleep(1)

# Вводим текст "999"
input_field.send_keys("999")

# Задержка для наглядности
time.sleep(1)

# Закрытие браузера
driver.quit()
