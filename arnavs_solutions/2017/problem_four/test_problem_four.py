from problem_four import fibonacci

import pytest

FIBONACCI_TEST_CASES = [
    (1, 1),
    (5, 3),
    (8, 13),
    (11, 55),
    (13, 144),
    (21, 6765),
    (40, 63245986),
    (2, 1),
    (9, 21),
    (90, 1779979416004714189)
]

@pytest.mark.parametrize("inp, output", FIBONACCI_TEST_CASES)
def test_fibonacci(inp, output):
    assert fibonacci(inp) == output
