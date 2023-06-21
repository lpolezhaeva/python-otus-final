from page_objects.MainPage import MainPage


def test_check_empty_shopping_card_label(browser):
    MainPage(browser).check_empty_shopping_card_label()


def test_change_currency(browser):
    MainPage(browser).change_currency("$ US Dollar")
