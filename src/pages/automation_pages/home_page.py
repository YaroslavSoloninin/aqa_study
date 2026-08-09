from playwright.sync_api import Page

import allure
from src.models.item import Item
from src.pages.automation_pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__items_names = page.locator(".productinfo p")
        self.__items_ids = page.locator("img[src^='/get_product_picture']")

    @allure.step("Получаем все товары")
    def get_items(self) -> list[Item]:
        items = []
        for item_id, item_name in zip(self.__items_ids.all(), self.__items_names.all()):
            src_attr = item_id.get_attribute("src")
            if src_attr is not None:
                id = int(src_attr.rsplit("/")[-1])
            name = item_name.text_content()
            if name is not None:
                clean_name = name.replace("\xa0", "").strip()
                items.append(Item(id, clean_name))
        return items
