from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск веб-браузера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода для имени пользователя и вводим значение "tomsmith"
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле ввода для пароля и вводим значение "SuperSecretPassword!"
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Находим кнопку "Login" и кликаем на неё
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Задержка для наглядности
time.sleep(2)

# Закрытие браузера
driver.quit()
