import pytest
import problem_eleven as p11

nums = (("0 176 80 30 12 184 90 132 101 76","132 101 76"),("0 176 80 10 12 184 90 132 101 76","12 184 90"),("0 176 80 30 100 95 93 147 113 87","100 95 93"))

@pytest.mark.parameterize("x","y")
def test_chrom(x,y):
    assert(chrom(x)==y)
