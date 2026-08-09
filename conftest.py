from typing import Any, Generator

import pytest
from playwright.sync_api import Page, sync_playwright

from src.allure.allure_reporter import AllureReporter
from src.api.jsonplaceholder import JsonPlaceholderAPI
from src.config import Config


@pytest.fixture
def json_placeholder_api() -> JsonPlaceholderAPI:
    return JsonPlaceholderAPI(Config.JSONPLACEHOLDER_URL, Config.TIMEOUT)


@pytest.fixture(scope="function")
def page() -> Generator[Page, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo[Any]
) -> Generator[None, Any, None]:
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = getattr(item, "funcargs", {}).get("page")
        if page:
            AllureReporter.attach_on_failure(page, item.name)
