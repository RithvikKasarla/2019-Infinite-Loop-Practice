import pytest as pyt
import problem_one as p1
passed = {70, 87, 100}
failed = {0, 48, 69}


@ pyt.mark.parametrize("x", passed)
def test_if_pass(x):
    assert p1.pass_fail(x) == "PASS"


@ pyt.mark.parametrize("y", failed)
def test_if_fail(y):
    assert p1.pass_fail(y) == "FAIL"
