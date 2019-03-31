import pytest
from new_problem_six import determine_led_states

TESTED_LED_STATES = [
    ("WORKING WORKING WORKING WORKING", "off off"),
    ("WORKING BROKEN BROKEN WORKING", "red green"),
    ("BROKEN BROKEN BROKEN BROKEN", "blue blue"),
    ("BROKEN BROKEN BROKEN WORKING", "red blue"),
    ("WORKING WORKING WORKING BROKEN", "green off"),
    ("BROKEN WORKING WORKING WORKING", "off red"),
]


@pytest.mark.parametrize("inp, output", TESTED_LED_STATES)
def test_solution(inp, output):
    assert determine_led_states(inp) == output
