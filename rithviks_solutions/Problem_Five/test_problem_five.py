import pytest
import problem_five as p5

stuff = (("12","12:10"),
("1024","1024:11"),
("100","100:26"),
("4","4:3"),
("12345","2345:51"))

@pytest.mark.parameterize("x, y", stuff)
def test_p5(x,y):
    assert(stuff[x] == y)
    