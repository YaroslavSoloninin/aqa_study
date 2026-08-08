from src.pages.home_page import HomePage
from src.pages.products_page import ProductsPage
from src.config import Config
from tests.test_data.test_data import TestData


class TestMultiPageFlow:
    def test_add_to_cart(self, page):
        page.goto(Config.BASE_URL)
        home_page = HomePage(page)
        home_page.top_menu.click_products_button()
        products_page = ProductsPage(page)
        product_detail_page = products_page.open_product_page_by_id(TestData.PRODUCT_ID)
        product_detail_page.add_product_to_cart()
        cart_page = product_detail_page.click_cart_button_modal()
        items = cart_page.get_items()
        assert len(items) == TestData.PRODUCTS_COUNT
        assert items[0].id == TestData.PRODUCT_ID
