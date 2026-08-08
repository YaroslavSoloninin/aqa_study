from datetime import datetime

import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_message():
    print(f"\nФикстура создана {datetime.now().isoformat()}")
    yield
    print(f"Фикстура удалена {datetime.now().isoformat()}")


@pytest.fixture()
def teardown_message():
    yield
