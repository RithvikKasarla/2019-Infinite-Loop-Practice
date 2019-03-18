import pytest
import Problem_Ten as p10

moves = (("8,8\n1,1\n8,8","Yes"),("10,20\n5,6\n7,8","Yes"),("100,100\n50,50\n20,21","No"))

@pytest.mark.parameterize("x","y")

def test_move(x,y):
    assert(p10.move(x)==y)
