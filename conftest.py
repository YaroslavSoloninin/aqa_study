import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_message():
    print()
    print("Фикстура модуля")


@pytest.fixture()
def teardown_message():
    yield
    print()
    print("Фикстура функции")
