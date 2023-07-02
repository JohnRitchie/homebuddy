from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def _click_to_element(self, element):
        self.browser.find_element(*element).click()
        
    def _fill_input(self, field, value):
        self.browser.find_element(*field).send_keys(value)

    def _element_is_visible(self, locator, timeout=15):
        self._go_to_element(self.element_is_present(locator))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def _go_to_element(self, element):
        try:
            self.browser.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True
    
    def open(self):
        self.browser.get(self.url)

    def click_to_visible_element(self, element):
        self._element_is_visible(element)
        self._click_to_element(element)

    def fill_visible_input(self, field, value):
        self._element_is_visible(field)
        self._fill_input(field, value)

    def element_is_present(self, locator, timeout=15):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def get_text(self, element):
        return self.browser.find_element(*element).text
