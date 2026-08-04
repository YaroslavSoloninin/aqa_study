from playwright.sync_api import Page

from src.pages.automation_pages.base_page import BasePage
from src.models.item import Item


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__items_names = page.locator(".productinfo p")
        self.__items_ids = page.locator("img[src^='/get_product_picture']")
        self.__cookie_consent = page.get_by_role("dialog")
        self.__cookie_accept_button = page.get_by_text("Соглашаюсь")

    def get_items(self) -> list[Item]:
        items = []
        for item_id, item_name in zip(
            self.__items_ids.all(), 
            self.__items_names.all()
        ):
            id = item_id.get_attribute("src").rsplit('/')[-1]
            name = item_name.text_content()
            items.append(Item(id, name))
        return items

    def accept_cookie(self):
        if self.__cookie_accept_button.is_visible(timeout=5000):
            self.__cookie_accept_button.click()
