from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск веб-браузера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Проверка наличия модального окна
modal = driver.find_element(By.ID, "modal")

# Проверяем, что модальное окно отображается
if modal.is_displayed():
    # Находим кнопку "Close" и кликаем на неё
    close_button = modal.find_element(By.XPATH, "//div[@id='modal']//a[text()='Close']")
    close_button.click()

# Закрытие браузера
driver.quit()