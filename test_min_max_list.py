import pytest


@pytest.mark.parametrize("list, expected_min, expected_max", [
    ([1, 2, 3, 4, 5], 1, 5),
    ([5, 10, -100, 0, 500], -100, 500),
    ([1, 1, 1, 1], 0, 0)
])
def test_min_max_list(list, expected_min, expected_max):
    from min_max_list import min_max_list
    min, max = min_max_list(list)
    assert min == expected_min
    assert max == expected_max
