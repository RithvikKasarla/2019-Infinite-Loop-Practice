import pytest

from new_problem_one import pass_or_fail

PASS_OR_FAIL_GRADES = [
    (0, "FAIL"),
    (1, "FAIL"),
    (48, "FAIL"),
    (69, "FAIL"),
    (70, "PASS"),
    (87, "PASS"),
    (100, "PASS"),
]


@pytest.mark.parametrize("inp, output", PASS_OR_FAIL_GRADES)
def test_solution(inp, output):
    assert pass_or_fail(inp) == output
