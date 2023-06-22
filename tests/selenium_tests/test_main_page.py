from page_objects.MainPage import MainPage
import allure


@allure.feature("Main page")
@allure.title("Check empty shopping card label")
def test_check_empty_shopping_card_label(browser):
    MainPage(browser).check_empty_shopping_card_label()


@allure.feature("Main page")
@allure.title("Change currency")
def test_change_currency(browser):
    MainPage(browser).change_currency("$ US Dollar")
