import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from datetime import datetime


@pytest.fixture(scope='function')
def browser():
    """Chrome is default"""

    print("\nstart browser")

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser

    screenshot = browser.get_screenshot_as_png()
    allure.attach(screenshot, name=f'Screenshot {datetime.today()}',
                  attachment_type=allure.attachment_type.PNG)

    print("\nquit browser")
    browser.quit()
    