from problem_three import addiply

import pytest

ADDIPLY_TEST_CASES = [
    ("2 2", "4 4"),
    ("5 4", "9 20"),
    ("3 8", "11 24"),
    ("1 1", "2 1"),
    ("445 442", "887 196690"),
    ("186 11545611", "11545797 2147483646")
]

@pytest.mark.parametrize("inp, output", ADDIPLY_TEST_CASES)
def test_addiply(inp, output):
    assert addiply(inp) == output
