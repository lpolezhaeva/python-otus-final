from page_objects.AdminMainPage import AdminMainPage
from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.ProductsPage import ProductsPage
import allure

PRODUCT_NAME = "Lenovo Think Pad 2.0"
NEW_PRODUCT_NAME = "Apple Cinema 30 [EDITED]"
COPY_PRODUCT_NAME = "iMac"


@allure.feature("Product page")
@allure.title("Validate a product form")
def test_product_validation(browser):
    with allure.step("Login as Admin user"):
        AdminLoginPage(browser).login_as_admin()
    with allure.step("Open Products page"):
        AdminMainPage(browser).open_products_page()
    with allure.step("Validate product"):
        ProductsPage(browser).validate_product()


@allure.feature("Product page")
@allure.title("Create a new product")
def test_product_creation(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).create_product(PRODUCT_NAME)


@allure.feature("Product page")
@allure.title("Edit a product")
def test_product_editing(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).edit_product(NEW_PRODUCT_NAME)


@allure.feature("Product page")
@allure.title("Copy an existing product")
def test_product_copying(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).copy_product()


@allure.feature("Product page")
@allure.title("Delete all products")
def test_all_product_deletion(browser):
    AdminLoginPage(browser).login_as_admin()
    AdminMainPage(browser).open_products_page()
    ProductsPage(browser).delete_product(PRODUCT_NAME)
