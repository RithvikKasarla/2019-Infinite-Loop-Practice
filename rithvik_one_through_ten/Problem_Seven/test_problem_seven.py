import  pytest
import problem_seven as p7

words = ((("Madam","AbBa","123321","$a3*3A$"),"TRUE"),(("RADAR","AbaB","SAGAS","wow","12345"),"False - 2,5"))


@pytest.mark.paramerterize("x","answer")
def test_palin(x,answer):
    assert(p7.palin(x)) == answer