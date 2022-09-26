import pytest


@pytest.mark.parametrize("a, b, expected", [
    (10, 32, -22),
    (10, 5, 5),
    (5, 5, 5)
])
def test_subtract(a, b, expected):
    from subtractor import subtract
    answer = subtract(a, b)
    assert answer == expected
