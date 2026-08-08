from playwright.sync_api import Page

from src.pages.automation_pages.base_page import BasePage
from src.models.item import Item


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.items = page.locator("a[href^='/product_details']")

    def get_items(self) -> list[Item]:
        items = []
        for item in self.items.all():
            id = int(item.get_attribute("href").rsplit("/")[-1])
            name = item.text_content()
            items.append(Item(id, name))
        return items
