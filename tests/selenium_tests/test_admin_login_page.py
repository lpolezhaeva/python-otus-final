from page_objects.AdminLoginPage import AdminLoginPage
import allure


@allure.feature("Login page")
@allure.title("Check elements on page")
def test_admin_login_page(browser):
    AdminLoginPage(browser).check_elements_on_page()


@allure.feature("Login page")
@allure.title("Check login validation")
def test_admin_login_validation(browser):
    AdminLoginPage(browser).check_validation()
