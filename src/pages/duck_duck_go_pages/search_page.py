from playwright.sync_api import Page, Locator


class SearchPage:
    def __init__(self, page: Page) -> None:
        self.__search_results = page.locator("article[data-testid='result']")

    def get_search_resulsts(self) -> list[Locator]:
        return self.__search_results.all()
