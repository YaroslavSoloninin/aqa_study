from playwright.sync_api import Page

import allure
from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__features_section = (
            page.get_by_text("Features Items").locator("..").locator("..")
        )
        self.__items_names = page.locator(".productinfo p")
        self.__items_ids = page.locator("img[src^='/get_product_picture']")

    @allure.step("Получаем все товары")
    def get_items(self) -> list[str]:
        product_names = [
            el.inner_text().strip()
            for el in self.__features_section.locator(".productinfo p").all()
            if el.is_visible()
        ]
        return product_names
