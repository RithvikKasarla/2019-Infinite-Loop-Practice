from problem_two import remove_letter_at_index

import pytest

REMOVE_LETTER_TEST_CASES = [
    ("puppy 0", "uppy"),
    ("kitten 4", "kittn"),
    ("fish 1", "fsh"),
    ("dog 2", "do"),
    ("a 0", ""),
    ("abcde 4", "abcd"),
]


@pytest.mark.parametrize("inp, output", REMOVE_LETTER_TEST_CASES)
def test_remove_letter_at_index(inp, output):
    assert remove_letter_at_index(inp) == output
