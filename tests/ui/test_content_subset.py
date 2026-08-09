import pytest

import allure
from src.config import Config
from src.pages.home_page import HomePage
from tests.test_data.test_data import TestData


@pytest.mark.ui
class TestContentSubset:
    def test_content(self, page):
        with allure.step("1. Переходим на главную страницу"):
            page.goto(Config.BASE_URL)
            home_page = HomePage(page)

        with allure.step("2. Проверяем, что основные товары есть на странице"):
            items_names = home_page.get_items()
            assert TestData.KEY_PRODUCTS_NAMES.issubset(items_names)
