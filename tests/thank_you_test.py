import allure
from pages.siding_order_page import SidingDeliveryPage
from pages.thank_you_page import ThankYouPage
from data import Link, AnswerData, ThankYouData
from helpers import HelperRandom


@allure.suite('Test thank you page')
class TestThankYou:

    @allure.feature('Check thank you page after basic ordering scenario')
    class TestBasicThankYou:

        @allure.title('Test opening a new order window, executing simple order and check if name is correct')
        def test_correct_name_after_order(self, browser):
            zip_code = AnswerData.zip_code
            siding_area = AnswerData.siding_area
            full_name = HelperRandom.get_full_name()
            name = full_name.split()[0]
            email = HelperRandom.get_email_address()
            phone = HelperRandom.get_phone_number()

            page_siding = SidingDeliveryPage(browser, Link.siding_link)
            page_thank_you = ThankYouPage(browser, Link.thank_you_link)
            page_siding.open()

            page_siding.make_order(zip_code, siding_area, full_name, email, phone)
            page_thank_you.wait_for_confirmation_text()
            thank_you_name = page_thank_you.get_thank_you_name()

            assert thank_you_name == name, 'Thank you name is not customer name!'

        @allure.title('Test opening a new order window, executing simple order and check if contractor is correct')
        def test_correct_contractor_after_order(self, browser):
            zip_code = AnswerData.zip_code
            siding_area = AnswerData.siding_area
            full_name = HelperRandom.get_full_name()
            name = full_name.split()[0]
            email = HelperRandom.get_email_address()
            phone = HelperRandom.get_phone_number()
            contractor = ThankYouData.contractor

            page_siding = SidingDeliveryPage(browser, Link.siding_link)
            page_thank_you = ThankYouPage(browser, Link.thank_you_link)
            page_siding.open()

            page_siding.make_order(zip_code, siding_area, full_name, email, phone)
            page_thank_you.wait_for_confirmation_text()
            thank_you_contractor = page_thank_you.get_thank_you_contractor()

            assert thank_you_contractor == contractor, 'Thank you contractor is not correct!'
