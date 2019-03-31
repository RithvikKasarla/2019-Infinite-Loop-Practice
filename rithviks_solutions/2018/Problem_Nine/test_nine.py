import pytest
import Problem_nine as p9

E = (("10,17", "17-10=7\n10-7=3\n7-3=4\n4-3=1\n3-1=2\n2-1=1\n1-1=0\nCOPRIME"),("56,26","56-26=30\n30-26=4\n26-4=22\n22-4=18\n18-4=14\n14-4=10\n10-4=6\n6-4=2\n4-2=2\n2-2=0\nNOT COPRIME"))

@pytest.mark.parameterize("x","y")

def test_math(x,y):
    assert(p9.Math(x)==y)
