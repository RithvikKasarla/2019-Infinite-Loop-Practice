import pytest
from new_problem_two import count_vowels

COUNTED_VOWELS = [
    ("code quest is fun", 6),
    ("good luck programming today", 8),
    ("queueing has five vowels in a row", 13),
    ("", 0),
    ("n0 v0w3ls", 0),
    ("aeiouaeiou", 10),
    ("a", 1),
]


@pytest.mark.parametrize("inp, output", COUNTED_VOWELS)
def test_solution(inp, output):
    assert count_vowels(inp) == output
