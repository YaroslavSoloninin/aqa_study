import pytest
from playwright.sync_api import Page, expect

from src.config import Config
from src.pages.main_page import MainPage


@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
def test_duckduckgo_search_parametrized(page: Page, query: str) -> None:
    page.goto(Config.BASE_URL)
    main_page = MainPage(page)
    search_page = main_page.search(query)
    results = search_page.get_search_resulsts()
    assert len(results) >= 5
    expect(results[0]).to_be_visible(timeout=10000)
