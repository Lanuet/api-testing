import pytest


@pytest.mark.parametrize("input, expected", [("3+4", 7), ("4+5", 8)])
def test_sum(input, expected):
    assert eval(input) == expected
