from playwright.sync_api import Page

from src.pages.automation_pages.base_page import BasePage
from src.pages.automation_pages.cart_page import CartPage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.__view_cart_button_modal = page.get_by_role("link", name="View Cart")

    def add_product_to_cart(self):
        self.__add_to_cart_button.click()

    def click_cart_button_modal(self) -> CartPage:
        self.__view_cart_button_modal.click()
        return CartPage(self.page)
