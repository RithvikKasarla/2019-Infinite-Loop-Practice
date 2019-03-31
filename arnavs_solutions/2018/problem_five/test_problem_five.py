import pytest
from new_problem_five import collatz_conjecture

COLLATZ_CONJECTURE_TESTED = [
    (12, "12:10"),
    (1024, "1024:11"),
    (100, "100:26"),
    (4, "4:3"),
    (12345, "12345:51"),
    (2, "2:2"),
    (1000000, "1000000:153"),
]

@pytest.mark.parametrize("inp, output", COLLATZ_CONJECTURE_TESTED)
def test_solution(inp, output):
    assert collatz_conjecture(inp) == output
