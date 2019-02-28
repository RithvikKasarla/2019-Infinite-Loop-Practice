import pytest as pyt
import problem_one as p1
inp = {70,87,100}
fail = {0,48,69}
@ pyt.mark.parametrize("x",inp)
def test_If_pass(x):
    assert p1.Pass_Fail(x) == "PASS"

@ pyt.mark.parametrize("y",fail)
def test_If_fail(y):
    assert p1.Pass_Fail(y) == "FAIL"
