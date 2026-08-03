import pytest

from src.config import Config
from src.pages.home_page import HomePage
from tests.test_data.test_data import TestData


@pytest.mark.ui
class TestContentSubset:
    def test_content(self, page):
        page.goto(Config.BASE_URL)
        home_page = HomePage(page)
        items_names = [item.name for item in home_page.get_items()]
        print(items_names)
        assert TestData.KEY_PRODUCTS_NAMES.issubset(items_names)
