import pytest as pyt
import problem_three as p3


@ pyt.mark.parametrize(x, "1st")
def test_problem_first(x):
    assert p3.suf(x) == "1st"


@ pyt.mark.parametrize(y, "10th")
def test_problem_first(y):
    assert p3.suf(y) == "10th"
