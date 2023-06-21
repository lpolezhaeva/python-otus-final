from selenium.webdriver.common.by import By
from ..BasePage import BasePage

import helpers


class TableRow(BasePage):
    SELF = (By.CSS_SELECTOR, "tr")
    CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    IMAGE = (By.CSS_SELECTOR, "img")
    TITLE = (By.CSS_SELECTOR, ".text-left")

    def get_row_text(self):
        return self.element(self.TITLE).text

    def check_row_text(self, text):
        return self.element(self.TITLE).text == text

    def check_row_checkbox(self):
        return self.element(self.CHECKBOX).click()
