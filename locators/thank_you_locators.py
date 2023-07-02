from selenium.webdriver.common.by import By


class ThankYouLocators:
    CONFIRMATION_TEXT = (By.XPATH, './/h4[contains(text(), "Thank you")]')
