import allure

from page_objects.RegistrationPage import RegistrationPage


@allure.feature("Registration")
@allure.title("Register new user")
def test_registration(browser):
    RegistrationPage(browser).check_elements_on_page()
    RegistrationPage(browser).register_new_user()


@allure.feature("Registration")
@allure.title("New user form validation")
def test_registration_validation(browser):
    RegistrationPage(browser).check_elements_on_page()
    RegistrationPage(browser).validate_required_fields()
