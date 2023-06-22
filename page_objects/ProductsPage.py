from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from page_objects.BasePage import BasePage
from page_objects.elements.ProductFormGeneral import ProductFormGeneral
from page_objects.elements.ProductFormData import ProductFormData
from page_objects.elements.FilterForm import FilterForm
from page_objects.elements.TableRow import TableRow


class ProductsPage(BasePage):
    CREATE_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Add New']")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Save']")
    COPY_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Copy']")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    EDIT_PRODUCT_BUTTON = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    NAV_TAB_GENERAL = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(1) > a")
    NAV_TAB_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    PRODUCT_FORM = (By.CSS_SELECTOR, "#form-product")
    SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]")
    FIRST_ITEM_CHECKBOX = (By.CSS_SELECTOR, "input[value='42']")
    PRODUCT_TABLE = (By.CSS_SELECTOR, "#form-product > div > table")

    def get_table_rows(self):
        return self.element(self.PRODUCT_TABLE).find_elements(By.TAG_NAME, "tr")

    def get_table_row(self, index=0):
        rows = self.driver.find_elements(By.TAG_NAME, "tr")
        return rows[index]

    def click_add_new_product_button(self):
        self.element(self.CREATE_NEW_PRODUCT_BUTTON).click()

    def click_edit_product_button(self):
        self.element(self.EDIT_PRODUCT_BUTTON).click()

    def click_copy_product_button(self):
        self.element(self.COPY_PRODUCT_BUTTON).click()

    def click_save_product_button(self):
        self.element(self.SAVE_PRODUCT_BUTTON).click()

    def click_first_checkbox(self):
        self.element(self.FIRST_ITEM_CHECKBOX).click()

    def click_nav_tab_data(self):
        self.element(self.NAV_TAB_DATA).click()

    def check_success_message(self):
        return self.element(self.SUCCESS_MESSAGE).text.strip() == "Success: You have modified products!"

    def check_error_message(self):
        return self.element(self.ERROR_MESSAGE).text.strip() == "Warning: Please check the form carefully for errors!"

    def check_row_text(self, text):
        return self == text

    def check_empty_table(self):
        return len(self.get_table_rows()) == 2

    def create_product(self, product_name="ProductName1"):
        self.click_add_new_product_button()
        ProductFormGeneral(self.driver).fill_in_all_fields(product_name)
        self.click_nav_tab_data()
        ProductFormData(self.driver).fill_in_all_fields()
        self.click_save_product_button()
        self.check_success_message()

    def validate_product(self):
        self.click_add_new_product_button()

    def edit_product(self, new_product_name="ProductName1"):
        self.click_edit_product_button()
        ProductFormGeneral(self.driver).change_product_name(new_product_name)
        self.click_save_product_button()
        self.check_success_message()

    def copy_product(self):
        # TODO check - should we pass self.driver here?
        row = TableRow(self.get_table_row(2))
        row.check_row_checkbox()
        self.click_copy_product_button()
        self.check_success_message()
        # check copied row
        row_copied = TableRow(self.get_table_row(1))
        row_copied.check_row_text(text="HTC Touch HD")

    def delete_product(self, product_name):
        FilterForm(self.driver).filter_product_by_name(product_name)
        self.element(self.SELECT_ALL_CHECKBOX).click()
        self.element(self.DELETE_PRODUCT_BUTTON).click()
        Alert(self.driver).accept()
        self.check_success_message()
        # check empty list
        self.check_empty_table()
