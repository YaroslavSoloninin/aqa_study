from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.pages.product_detail_page import ProductDetailPage


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def open_product_page_by_id(self, product_id: int) -> ProductDetailPage:
        view_product_button = self.__product_link(product_id)
        view_product_button.click()
        return ProductDetailPage(self.page)

    def __product_link(self, product_id: int):
        return self.page.locator(f"a[href='/product_details/{product_id}']")
