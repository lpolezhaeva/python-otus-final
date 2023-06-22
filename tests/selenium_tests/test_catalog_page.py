from page_objects.CatalogPage import CatalogPage
import allure


@allure.feature("Catalog page")
@allure.title("Check elements on page")
def test_catalog_page(browser):
    CatalogPage(browser).check_elements_on_page()
