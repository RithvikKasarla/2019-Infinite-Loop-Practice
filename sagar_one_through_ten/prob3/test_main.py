import pytest
import main

test_cases = [
    ('0th', '0th'),
    ('12th', '12th'),
    ('22th', '22nd'),
    ('1th', '1st'),
    ('2th', '2nd'),
    ('3th', '3rd'),
    ('15th', '15th'),
    ('112th', "112th"),
    ('122th', '122nd'),
    ('-0th', '-0th'),
    ('-12th', '-12th'),
    ('-22th', '-22nd'),
    ('-1th', '-1st'),
    ('-2th', '-2nd'),
    ('-3th', '-3rd'),
    ('-15th', '-15th'),
    ('-112th', "-112th"),
    ('-122th', '-122nd')
]

@pytest.mark.parametrize('line, output', test_cases)
def test_suffix(line, output):
    assert(main.suffix(line) == output)
