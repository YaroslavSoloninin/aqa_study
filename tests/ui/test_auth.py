import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from src.config import Config
from src.pages.sauce_demo_pages.login_page import LoginPage
from tests.test_data.test_data import TestData

load_dotenv()


@pytest.mark.ui
class TestAuth:
    def test_successful_login(self, page: Page) -> None:
        login_page = LoginPage(page)
        page.goto(Config.SAUCE_DEMO_URL)
        username = os.getenv("SAUCE_USER", "standard_user")
        password = os.getenv("SAUCE_PASS", "secret_sauce")
        login_page.login(username, password)
        expect(page).to_have_url(TestData.URL_AFTER_LOGIN)

    def test_locked_out_user(self, page: Page) -> None:
        login_page = LoginPage(page)
        page.goto(Config.SAUCE_DEMO_URL)
        login_page.login(TestData.WRONG_USERNAME, TestData.WRONG_PASSWORD)
        error = login_page.get_error_message()
        assert TestData.PARTIAL_ERROR_MESSAGE in error
        assert page.url != TestData.URL_AFTER_LOGIN
