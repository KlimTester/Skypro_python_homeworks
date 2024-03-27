from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Запуск веб-браузера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликаем на кнопку "Add Element"
for _ in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()
    time.sleep(1)  # Ждем немного после каждого клика

# Находим все кнопки "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Выводим размер списка кнопок "Delete"
print("Размер списка кнопок 'Delete':", len(delete_buttons))

# Закрытие браузера
driver.quit()

