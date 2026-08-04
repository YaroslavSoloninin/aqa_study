from playwright.sync_api import Page
from typing import Self

from src.forms.top_menu import TopMenu


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.top_menu = TopMenu(page)

    def goto(self, url: str) -> Self:
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")
        return self

    def wait_for_page_load(self) -> Self:
        self.page.wait_for_load_state("networkidle")
        return self
