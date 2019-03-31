from problem_one import echo_twice

import pytest

ECHO_TEST_CASES = [
    ("Code Quest rules!", "Code Quest rules!\nCode Quest rules!"),
    ("I’m definitely coming back next year.", "I’m definitely coming back next year.\nI’m definitely coming back next year."),
    ("aaaaaa", "aaaaaa\naaaaaa")
]

@pytest.mark.parametrize("inp, output", ECHO_TEST_CASES)
def test_echo_twice(inp, output):
    assert echo_twice(inp) == output
