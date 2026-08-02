import pytest

from src.tools.is_adult import is_adult


@pytest.mark.test
@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (25, True),
        (0, False),
    ],
    ids=[
        "underage_by_one_year",
        "exactly_min_valid_age",
        "adult_age",
        "zero_age",
    ],
)
def test_is_adult(age, expected):
    assert is_adult(age) == expected
