from selenium.webdriver.common.by import By


class SidingDeliveryPageLocators:
    # just first elements, without footer, etc.
    # and not all items possible for answers

    SUBMIT_BUTTON = (By.XPATH, './/button[@data-autotest-button-submit-0]')
    NEXT_BUTTON = (By.XPATH, './/button[@data-autotest-button-submit-next]')
    SUBMIT_REQUEST_BUTTON = (By.XPATH, './/button[@data-autotest-button-submit-submit-my-request]')
    CONFIRM_PHONE_BUTTON = (By.XPATH, './/button[@data-autotest-button-submit-phone-number-is-correct]')
    ZIP_CODE_INPUT = (By.ID, 'zipCode')

    # impersonal buttons
    FIRST_TYPE_OF_PROJECT_BUTTON = (By.XPATH, './/div[@class="typeOfProject defaultGrid mx-auto mb-4 mb-md-6"]/div[1]')
    FIRST_KIND_OF_SIDING_BUTTON = (By.XPATH, './/div[@class="kindOfSiding defaultGrid mx-auto mb-4 mb-md-6"]/div[1]')
    FIRST_NUMBER_OF_STORIES_BUTTON = (By.XPATH, './/div[@class="howManyStories__grid defaultGrid mx-auto mb-4 '
                                                'mb-md-6"]/div[1]')
    # FIRST_AUTHORIZATION_BUTTON = (By.XPATH, './/input[@data-autotest-radio-internalowner-1]')
    FIRST_AUTHORIZATION_BUTTON = (By.XPATH, './/div[@class="mb-2 mb-md-6 mx-md-2 KfTOGlBfinEjtYe5ZyDq"]')

    SIDING_AREA_INPUT = (By.XPATH, './/input[@data-autotest-input-squarefeet-tel]')
    FULL_NAME_INPUT = (By.XPATH, './/input[@data-autotest-input-fullname-text]')
    EMAIL_INPUT = (By.XPATH, './/input[@data-autotest-input-email-email]')
    PHONE_INPUT = (By.XPATH, './/input[@data-autotest-input-phonenumber-tel]')
