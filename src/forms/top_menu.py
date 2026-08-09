from playwright.sync_api import Page


class TopMenu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.__products_button = page.get_by_role("link", name="Products")

    def click_products_button(self) -> None:
        self.__products_button.click()
