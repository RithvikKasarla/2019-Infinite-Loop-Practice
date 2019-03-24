import pytest
from main import run

TESTS = [["Bob,Joe,Steve,Mary,Ann", "Bob,Steve,Ann,Paula,Chris", "Joe,Mary", "Ann,Bob,Steve", "Chris,Paula"],
        ["Bill,Ted,Liz,Quinn", "Quinn,Liz,Ken,Bill", "Ted", "Bill,Liz,Quinn", "Ken"]]

@pytest.mark.parametrize("a, b, c, d, e", TESTS)
def test_run(a, b, c, d, e):
        assert(run(a, b) == (c, d, e))