import allure

from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.siding_order_locators import SidingDeliveryPageLocators


class SidingDeliveryPage(BasePage):

    @allure.step('Enter zip code')
    def _answer_zip(self, number):
        with allure.step('Fill zip code'):
            self.fill_visible_input(SidingDeliveryPageLocators.ZIP_CODE_INPUT, number)
        with allure.step('Click to submit button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.SUBMIT_BUTTON)

    @allure.step('Choose type of project')
    def _answer_type_of_project(self):
        with allure.step('Click to first type of project'):
            self.click_to_visible_element(SidingDeliveryPageLocators.FIRST_TYPE_OF_PROJECT_BUTTON)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Choose kind of siding')
    def _answer_kind_of_siding(self):
        with allure.step('Click to first kind of siding'):
            self.click_to_visible_element(SidingDeliveryPageLocators.FIRST_KIND_OF_SIDING_BUTTON)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Answer how many square feet will be covered with new siding')
    def _answer_siding_area(self, number):
        with allure.step('Fill square feet'):
            self.fill_visible_input(SidingDeliveryPageLocators.SIDING_AREA_INPUT, number)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Choose how many stories a house has')
    def _answer_number_of_stories(self):
        with allure.step('Click to first number of stories'):
            self.click_to_visible_element(SidingDeliveryPageLocators.FIRST_NUMBER_OF_STORIES_BUTTON)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Answer obout homeowner or authorized to make property changes')
    def _answer_authorized(self):
        with allure.step('Click to Yes'):
            self.click_to_visible_element(SidingDeliveryPageLocators.FIRST_AUTHORIZATION_BUTTON)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Answer for whom you need to prepare this estimate')
    def _answer_name_and_email(self, name, mail):
        with allure.step('Fill full name'):
            self.fill_visible_input(SidingDeliveryPageLocators.FULL_NAME_INPUT, name)
        with allure.step('Fill email'):
            self.fill_visible_input(SidingDeliveryPageLocators.EMAIL_INPUT, mail)
        with allure.step('Click to next button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.NEXT_BUTTON)

    @allure.step('Answer phone number')
    def _answer_phone(self, number):
        with allure.step('Fill phone'):
            self.fill_visible_input(SidingDeliveryPageLocators.PHONE_INPUT, number)
        with allure.step('Click to submit button'):
            self.click_to_visible_element(SidingDeliveryPageLocators.SUBMIT_REQUEST_BUTTON)

    @allure.step('Confirm the phone number if necessary')
    def _confirm_phone(self):
        # self.click_to_visible_element(SidingDeliveryPageLocators.CONFIRM_PHONE_BUTTON)
        try:
            with allure.step('Check if phone confirmation is required'):
                button = self.element_is_present(SidingDeliveryPageLocators.CONFIRM_PHONE_BUTTON)
            with allure.step('Click to phone confirmation'):
                button.click()
        except TimeoutException:
            with allure.step('Print that phone confirmation is not required'):
                print("Confirm the phone number is not necessary, skip")

    def make_order(self, zip_code, siding_area, full_name, email, phone):
        self._answer_zip(zip_code)
        self._answer_type_of_project()
        self._answer_kind_of_siding()
        self._answer_siding_area(siding_area)
        self._answer_number_of_stories()
        self._answer_authorized()
        self._answer_name_and_email(full_name, email)
        self._answer_phone(phone)
        self._confirm_phone()
