from playwright.sync_api import Page

import allure
from src.pages.base_page import BasePage
from src.pages.cart_page import CartPage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.__view_cart_button_modal = page.get_by_role("link", name="View Cart")

    @allure.step("Добавляем товар в корзину")
    def add_product_to_cart(self) -> None:
        self.__add_to_cart_button.click()

    @allure.step("Открываем корзину")
    def click_cart_button_modal(self) -> CartPage:
        self.__view_cart_button_modal.click()
        return CartPage(self.page)
