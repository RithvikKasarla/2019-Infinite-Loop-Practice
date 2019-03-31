from problem_six import icao_version

import pytest

ICAO_TEST_CASES = [
    ("Code Quest", "Charlie-Oscar-Delta-Echo Quebec-Uniform-Echo-Sierra-Tango"),
    ("Rocks", "Romeo-Oscar-Charlie-Kilo-Sierra"),
    ("Lockheed", "Lima-Oscar-Charlie-Kilo-Hotel-Echo-Echo-Delta"),
    ("the quick", "Tango-Hotel-Echo Quebec-Uniform-India-Charlie-Kilo"),
    ("brOwn fox", "Bravo-Romeo-Oscar-Whiskey-November Foxtrot-Oscar-Xray"),
    (
        "JuMpS oVeR tHe",
        "Juliet-Uniform-Mike-Papa-Sierra Oscar-Victor-Echo-Romeo Tango-Hotel-Echo",
    ),
    ("laZY DOG", "Lima-Alpha-Zulu-Yankee Delta-Oscar-Golf"),
    ("EeEe", "Echo-Echo-Echo-Echo"),
    ("A", "Alpha"),
]


@pytest.mark.parametrize("inp, output", ICAO_TEST_CASES)
def test_icao_version(inp, output):
    assert icao_version(inp) == output
