from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.user_name_input = (By.CSS_SELECTOR, "#user-name")
        self.password_input = (By.CSS_SELECTOR, "#password")
        self.login_button = (By.CSS_SELECTOR, "#login-button")

    def open(self, url="http://www.saucedemo.com/"):
        self.driver.get(url)

    def login(self, username="standard_user", password="secret_sauce"):
        user_field = self.wait.until(
            EC.visibility_of_element_located(self.user_name_input))
        user_field.clear()
        user_field.send_keys(username)

        pass_field = self.driver.find_element(*self.password_input)
        pass_field.clear()
        pass_field.send_keys(password)

        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
