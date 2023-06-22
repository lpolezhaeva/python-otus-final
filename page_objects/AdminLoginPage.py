import logging

import allure
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage

logger = logging.getLogger(__name__)


class AdminLoginPage(BasePage):
    PANEL_TITLE = (By.CSS_SELECTOR, "h1.panel-title")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.CSS_SELECTOR, "#footer > a")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")

    USERNAME = "user"
    PASSWORD = "bitnami"

    def __init__(self, driver):
        super().__init__(driver)
        print("URL:", self.driver.url + "/admin")
        print("Current url:", self.driver.current_url)
        try:
            self.driver.get(self.driver.url + "/admin")
            import time
            time.sleep(10)
        except Exception as e:
            logger.exception(e)
            print("Refused url:", self.driver.current_url)
            raise e

    def check_error_message(self):
        return self.element(self.ERROR_MESSAGE) == " No match for Username and/or Password."

    def check_elements_on_page(self):
        self.element(self.PANEL_TITLE)
        self.element(self.USERNAME_INPUT)
        self.element(self.PASSWORD_INPUT)
        self.element(self.SUBMIT_BUTTON)
        self.element(self.OPENCART_LINK)
        self.element(self.FORGOTTEN_PASSWORD)

    def login_as_admin(self):
        self._send_keys(self.USERNAME_INPUT, self.USERNAME)
        self._send_keys(self.PASSWORD_INPUT, self.PASSWORD)
        try:
            self.element(self.SUBMIT_BUTTON).click()
        except Exception as e:
            logger.error("Got exception")
            logger.exception(e)

            allure.attach(
                name="Screenshot",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.save_screenshot()
            raise e

    def check_validation(self):
        self.element(self.SUBMIT_BUTTON).click()
        self.check_error_message()
