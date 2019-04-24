from problem_seven import slugging_percentage

import pytest

SLUGGING_PERCENTAGE_TEST_CASES = [
    ("Moreland:K,2B,1B,HR", "Moreland=1.750"),
    ("Andrus:BB,BB,2B,K", "Andrus=1.000"),
    ("Chirinos:1B,1B,3B", "Chirinos=1.667"),
    ("Odor:1B,K,3B", "Odor=1.333"),
    ("A:BB", "A=0.000"),
    ("A:K,K,K,K,BB", "A=0.000"),
    ("A:HR,HR,HR,HR,HR,HR,HR,HR,HR,HR", "A=4.000"),
]


@pytest.mark.parametrize("inp, output", SLUGGING_PERCENTAGE_TEST_CASES)
def test_slugging_percentage(inp, output):
    assert slugging_percentage(inp) == output
