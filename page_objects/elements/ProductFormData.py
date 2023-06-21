from selenium.webdriver.common.by import By
from ..BasePage import BasePage

import helpers


class ProductFormData(BasePage):
    SELF = (By.CSS_SELECTOR, "tab-data")
    PRODUCT_MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")

    def fill_in_all_fields(self):
        self._send_keys(self.PRODUCT_MODEL_INPUT, helpers.random_string())
