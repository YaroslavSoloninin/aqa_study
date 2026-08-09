from typing import Any, Generator
from datetime import datetime
import pytest
from playwright.sync_api import Page, sync_playwright
from src.allure.allure_reporter import AllureReporter


@pytest.fixture(scope="module", autouse=True)
def setup_message():
    print(f"\nФикстура создана {datetime.now().isoformat()}")
    yield
    print(f"Фикстура удалена {datetime.now().isoformat()}")


@pytest.fixture()
def teardown_message():
    yield


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
