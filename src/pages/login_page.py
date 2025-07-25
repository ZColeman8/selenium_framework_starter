from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.logger import logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        logger.info("Entering username")
        field = self.wait.until(EC.element_to_be_clickable(self.username_input))
        field.clear()
        field.send_keys(username)
        logger.debug(f"Username entered: {username}")

    def enter_password(self, password):
        logger.info("Entering password")
        field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        field.clear()
        field.send_keys(password)
        logger.debug("Password entered (hidden)")

    def click_login(self):
        logger.info("Clicking login button")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()