import pytest
from playwright.sync_api import Page

import allure
from src.config.config import Config
from src.pages.automation_pages.home_page import HomePage
from src.pages.automation_pages.products_page import ProductsPage
from tests.test_data.test_data import TestData as TD


@pytest.mark.ui
class TestMultiPageFlow:
    def test_add_to_cart(self, page: Page) -> None:
        with allure.step("1. Переходим на главную страницу"):
            page.goto(Config.AUTOMATION_EXERCISE_URL)
            home_page = HomePage(page)

        with allure.step("2. Переходим на страницу с товарами"):
            home_page.top_menu.click_products_button()
            products_page = ProductsPage(page)

        with allure.step(f"3. Открываем страницу товара с id={TD.PRODUCT_ID}"):
            product_detail_page = products_page.open_product_page_by_id(TD.PRODUCT_ID)

        with allure.step(f"4. Добавляем товар c id={TD.PRODUCT_ID} в корзину"):
            product_detail_page.add_product_to_cart()

        with allure.step("5. Открываем корзину"):
            cart_page = product_detail_page.click_cart_button_modal()
            with allure.step("Проверяем, что товар в корзине"):
                items = cart_page.get_items()
                assert len(items) == TD.PRODUCTS_COUNT
                assert items[0].id == TD.PRODUCT_ID
