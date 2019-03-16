import pytest
import problem_eight as p8

lines = (("356.69 163.42 346.67","176.69 343.42 166.67"),("302.26 345.92 011.79","122.26 165.92 191.79"))

@pytest.mark.parameterize("x","y")

def test_apollo(x,y):
    assert(p8.apollo(x)) == y
