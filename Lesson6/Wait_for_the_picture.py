from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//img[@alt='Image 4'] | //div[text()='Done']"))
)

third_image_src = driver.find_element_by_xpath("//img[@alt='Image 3']").get_attribute("src")

print("SRC атрибут третьей картинки:", third_image_src)
driver.quit()