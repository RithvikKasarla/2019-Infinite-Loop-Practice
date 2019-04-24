import pytest
import prob3 as p3
TESTS = [["3 5","8 15"],
        ["1 7" , "8 7"],
        ["2 2", "4 4"],
        ["5 4", "9 20"],
        ["3 8", "11 24"],
        ["0 0", "0 0"],
        ["-1 3", "2 -3"],
        ]

@pytest.mark.parametrize("x , y",TESTS)

def test_addiply(x,y):
    assert(p3.addiply(x)==y)