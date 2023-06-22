import allure
from selenium.webdriver.common.by import By

import helpers
from page_objects.BasePage import BasePage


class RegistrationPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1")
    ACCOUNT_LEGEND = (By.CSS_SELECTOR, "#account > legend")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-confirm")
    NEWSLETTER_RADIO_YES = (By.CSS_SELECTOR, "input[type='radio'][name='newsletter'][value='1']")
    NEWSLETTER_RADIO_NO = (By.CSS_SELECTOR, "input[type='radio'][name='newsletter'][value='0']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "a.agree")

    SUCCESS_MESSAGE_HEADER = (By.CSS_SELECTOR, "#content > h1")
    SUCCESS_MESSAGE_PARAGRAPH = (By.CSS_SELECTOR, "#content > p")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#account-register > div.alert.alert-danger.alert-dismissible")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/index.php?route=account/register")

    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.ACCOUNT_LEGEND)
        self.element(self.FIRSTNAME_INPUT)
        self.element(self.LASTNAME_INPUT)
        self.element(self.EMAIL_INPUT)
        self.element(self.TELEPHONE_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.CONFIRM_PASSWORD_INPUT)
        self.element(self.NEWSLETTER_RADIO_YES)
        self.element(self.NEWSLETTER_RADIO_NO)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.PRIVACY_POLICY_CHECKBOX)
        self.element(self.PRIVACY_POLICY_LINK)

    def input_all_fields(self):
        user_first_name = helpers.random_string(5)
        user_last_name = helpers.random_string(5)
        password = helpers.random_string(10)
        self._send_keys(self.FIRSTNAME_INPUT, user_first_name)
        self._send_keys(self.LASTNAME_INPUT, user_last_name)
        self._send_keys(self.EMAIL_INPUT, helpers.random_email())
        self._send_keys(self.TELEPHONE_INPUT, helpers.random_phone())
        self._send_keys(self.PASSWORD_INPUT, password)
        self._send_keys(self.CONFIRM_PASSWORD_INPUT, password)
        self.element(self.PRIVACY_POLICY_CHECKBOX).click()
        self.element(self.SUBMIT_BUTTON).click()

    def check_registration_success(self):
        return self.element(self.SUCCESS_MESSAGE_HEADER) == "Your Account Has Been Created!" and \
               self.element(self.SUCCESS_MESSAGE_PARAGRAPH) == "Congratulations! Your new account has been " \
                                                               "successfully created! "

    def check_error_message(self):
        return self.element(self.ERROR_MESSAGE) == " Warning: You must agree to the Privacy Policy!"

    def register_new_user(self):
        with allure.step("Fill in all fields"):
            self.input_all_fields()
        with allure.step("Check the messages after a user registration"):
            self.check_registration_success()

    def validate_required_fields(self):
        self.element(self.SUBMIT_BUTTON).click()
        self.check_error_message()
