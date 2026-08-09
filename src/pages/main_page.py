from playwright.sync_api import Page

from src.pages.search_page import SearchPage

class MainPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.__search_input = page.get_by_placeholder("Конфиденциальный поиск")

    def search(self, query: str) -> SearchPage:
        self.__search_input.fill(query)
        with self.page.expect_navigation():
            self.__search_input.press("Enter")
        self.page.wait_for_load_state("load")
        return SearchPage(self.page)
