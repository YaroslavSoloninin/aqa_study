from playwright.sync_api import Page

import allure
from src.models.item import Item
from src.pages.automation_pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.items = page.locator("a[href^='/product_details']")

    @allure.step("Получаем список товаров в корзине")
    def get_items(self) -> list[Item]:
        items = []
        for item in self.items.all():
            id = int(item.get_attribute("href").rsplit("/")[-1])  # type: ignore[union-attr]
            name = item.text_content()
            items.append(Item(id, name))  # type: ignore[arg-type]
        return items
