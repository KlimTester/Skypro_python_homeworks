from selenium.webdriver.common.by import By


class FillingTheFormPage():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def input_form_first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def input_form_last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def input_form_address(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def input_form_zip_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    def input_form_city(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def input_form_country(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def input_form_e_mail(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def input_form_phone(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def input_form_job_position(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def input_form_company(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def alert_danger(self):
        alert_danger = self._driver.find_element(By.CSS_SELECTOR, 'div.alert.py-2.alert-danger').value_of_css_property("background-color")
        return alert_danger

    def alert_success(self):
        allert_success = self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
        for form in allert_success:
            return form.value_of_css_property("background-color")