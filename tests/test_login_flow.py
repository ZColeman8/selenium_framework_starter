from src.pages.login_page import LoginPage
from src.utils.logger import logger

def test_login_flow(driver):
    logger.info("Starting login flow test")
    
    # Navigate to the SauceDemo login page
    driver.get("https://www.saucedemo.com/")
    logger.info("Navigated to SauceDemo")

    # Initialize the login page and perform login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Assertion: Check if login was successful by verifying URL
    assert "inventory" in driver.current_url, "Login failed: inventory page not reached"
    logger.info("Login flow test passed")