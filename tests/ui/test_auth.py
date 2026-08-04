import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

from src.pages.login_page import LoginPage
from src.config.config import Config
from tests.test_data.test_data import TestData

load_dotenv()


@pytest.mark.ui
class TestAuth:
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        page.goto(Config.BASE_URL)
        username = os.getenv("SAUCE_USER", "standard_user")
        password = os.getenv("SAUCE_PASS", "secret_sauce")
        login_page.login(username, password)
        expect(page).to_have_url(TestData.URL_AFTER_LOGIN)

    def test_locked_out_user(self, page):
        login_page = LoginPage(page)
        page.goto(Config.BASE_URL)
        login_page.login(TestData.WRONG_USERNAME, TestData.WRONG_PASSWORD)
        error = login_page.get_error_message()
        assert TestData.PARTIAL_ERROR_MESSAGE in error
        assert page.url != TestData.URL_AFTER_LOGIN
