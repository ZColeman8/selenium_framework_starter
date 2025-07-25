import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from src.utils.logger import logger


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run Chrome in headless mode")


@pytest.fixture
def driver(request):
    # Setup Chrome with optional headless
    headless = request.config.getoption("--headless")
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")
        logger.info("Running Chrome in headless mode")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logger.info("✅ WebDriver started")
    yield driver
    driver.quit()
    logger.info("✅ WebDriver closed")


# Screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join("screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            driver.save_screenshot(filepath)
            logger.error(f"❌ Test failed. Screenshot saved to: {filepath}")