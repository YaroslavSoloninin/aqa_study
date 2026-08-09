import pytest
from playwright.sync_api import Page

import allure
from src.config.config import Config
from src.pages.automation_pages.home_page import HomePage
from tests.test_data.test_data import TestData as TD


@pytest.mark.ui
class TestContentSubset:
    def test_content(self, page: Page) -> None:
        with allure.step("1. Переходим на главную страницу"):
            page.goto(Config.AUTOMATION_EXERCISE_URL)
            home_page = HomePage(page)

        with allure.step("2. Проверяем, что основные товары есть на странице"):
            items_names = home_page.get_items()
            assert TD.KEY_PRODUCTS_NAMES.issubset(items_names)
