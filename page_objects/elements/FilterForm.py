from selenium.webdriver.common.by import By
from ..BasePage import BasePage


class FilterForm(BasePage):
    SELF = (By.CSS_SELECTOR, "filter-product")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")

    def filter_product_by_name(self, product_name):
        self._send_keys(self.PRODUCT_NAME_INPUT, product_name)
        self.element(self.FILTER_BUTTON).click()
