from problem_five import donor_sort

import pytest

DONOR_SORT_TEST_CASES = [
    (["Bob,Joe,Steve,Mary,Ann", "Bob,Steve,Ann,Paula,Chris"], ["Joe,Mary", "Ann,Bob,Steve", "Chris,Paula"]),
    (["Bill,Ted,Liz,Quinn", "Quinn,Liz,Ken,Bill"], ["Ted", "Bill,Liz,Quinn", "Ken"]),
    (["a,b,c", "d,e,f"], ["a,b,c", "", "d,e,f"]),
    (["a,b,c", "f,e"], ["a,b,c", "", "e,f"]),
    (["", "f,e"], ["", "", "e,f"]),
    (["a,b,c", ""], ["a,b,c", "", ""]),
    (["", ""], ["", "", ""]),
]

@pytest.mark.parametrize("inp, output", DONOR_SORT_TEST_CASES)
def test_donor_sort(inp, output):
    assert donor_sort(*inp) == output
