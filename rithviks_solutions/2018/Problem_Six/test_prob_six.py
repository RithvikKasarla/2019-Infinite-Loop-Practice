import pytest
import problem_six as p6
error = ((("WORKING", "WORKING", "WORKING", "WORKING"), "off off"),
        (("WORKING", "BROKEN", "BROKEN", "WORKING"), "red green"),
        (("BROKEN", "BROKEN", "BROKEN", "BROKEN"), "blue blue"))
        

@pytest.mark.parameterize("line","solution")

def test_machine(line, solution):
    assert p6.machine(line) == solution
    