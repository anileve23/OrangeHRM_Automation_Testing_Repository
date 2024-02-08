from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self._username_field = (By.NAME, 'username')
        self._password_field = (By.NAME, 'password')
        self._login_button = (By.CSS_SELECTOR, 'button[data-v-10d463b7=""]')
        self._confirm_password_field = (By.CSS_SELECTOR, 'input.oxd-input[type="password"][autocomplete="off"][data-v-1f99f73c=""]')

    def fill_login_form(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self._username_field)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self._password_field)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._login_button)
        )
        login_button.click()

    def fill_confirm_password(self, confirm_password):
        confirm_password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self._confirm_password_field)
        )
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirm_password)