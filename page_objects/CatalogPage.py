from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h2")
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    COMPARE_TOTAL_LINK = (By.CSS_SELECTOR, "#compare-total")
    SORT_INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIMIT_INPUT = (By.CSS_SELECTOR, "#input-limit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.driver.url + "/desktops")

    def check_elements_on_page(self):
        self.element(self.HEADER)
        self.element(self.LIST_VIEW_BUTTON)
        self.element(self.GRID_VIEW_BUTTON)
        self.element(self.COMPARE_TOTAL_LINK)
        self.element(self.SORT_INPUT)
        self.element(self.LIMIT_INPUT)
