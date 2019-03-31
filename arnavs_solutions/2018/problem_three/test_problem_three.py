import pytest
from problem_three_two import correct_suffixes


CORRECTED_SUFFIXES = [
    ("0th", "0th"),
    ("1th", "1st"),
    ("2th", "2nd"),
    ("3th", "3rd"),
    ("4th", "4th"),
    ("10th", "10th"),
    ("11th", "11th"),
    ("12th", "12th"),
    ("13th", "13th"),
    ("-21th", "-21st"),
    ("22th", "22nd"),
    ("23th", "23rd"),
    ("100th", "100th"),
    ("404th", "404th"),
    ("123th", "123rd"),
]


@pytest.mark.parametrize("inp, output", CORRECTED_SUFFIXES)
def test_solution(inp, output):
    assert correct_suffixes(inp) == output
