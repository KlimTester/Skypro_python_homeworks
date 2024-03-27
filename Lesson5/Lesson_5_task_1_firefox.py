from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера Gecko
driver = webdriver.Firefox()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликаем на кнопку "Add Element"
for _ in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()
    time.sleep(1)  # Ждем немного после каждого клика

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Выводим на экран размер списка
print("Размер списка кнопок 'Delete':", len(delete_buttons))

# Закрытие браузера
driver.quit()