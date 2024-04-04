from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/textinput')
my_button = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
my_button.send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(txt)
driver.quit()