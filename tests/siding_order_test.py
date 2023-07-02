import allure
from pages.siding_order_page import SidingDeliveryPage
from pages.thank_you_page import ThankYouPage
from data import Link, AnswerData
from helpers import HelperRandom


@allure.suite('Test order page')
class TestOrder:

    @allure.feature('Basic ordering scenario')
    class TestBasicOrder:

        @allure.title('Test opening a new order window and executing simple order')
        def test_order(self, browser):
            zip_code = AnswerData.zip_code
            siding_area = AnswerData.siding_area
            full_name = HelperRandom.get_full_name()
            email = HelperRandom.get_email_address()
            phone = HelperRandom.get_phone_number()

            page_siding = SidingDeliveryPage(browser, Link.siding_link)
            page_thank_you = ThankYouPage(browser, Link.thank_you_link)
            page_siding.open()

            page_siding.make_order(zip_code, siding_area, full_name, email, phone)
            page_thank_you.wait_for_confirmation_text()

            assert browser.current_url == Link.thank_you_link, 'Thank you page is not open!'
