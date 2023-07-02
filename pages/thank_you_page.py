import allure

from pages.base_page import BasePage
from locators.thank_you_locators import ThankYouLocators


class ThankYouPage(BasePage):

    @allure.step('Get "thank you" text')
    def _get_thank_you_text(self):
        return self.get_text(ThankYouLocators.CONFIRMATION_TEXT)

    @allure.step('Wait for a "thank you" page')
    def wait_for_confirmation_text(self):
        with allure.step('Wait for a "thank you" text'):
            return self.element_is_present(ThankYouLocators.CONFIRMATION_TEXT)

    @allure.step('Get name from "thank you" page')
    def get_thank_you_name(self):
        text = self._get_thank_you_text()

        with allure.step('Get name from "thank you" text'):
            thank_you_name = text.split(',')[0].split()[-1]
        return thank_you_name

    @allure.step('Get contractor from "thank you" page')
    def get_thank_you_contractor(self):
        text = self._get_thank_you_text()

        with allure.step('Get contractor from "thank you" text'):
            thank_you_contractor = text.split('contractor')[-1].split('will')[0].strip()
        return thank_you_contractor
