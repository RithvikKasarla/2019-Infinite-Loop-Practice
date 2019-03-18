import pytest
from Prob17 import Winner

TEST_TIC_TAC_TOE = [
    ("O-X-OOXXX", "O-X-OOXXX = X WINS"),
    ("XOX-OXO-X", "XOX-OXO-X = X WINS"),
    ("X-O-XO--O", "X-O-XO--O = O WINS"),
    ("OXOXXOXOX", "OXOXXOXOX = TIE"),
    ("--X-X-XOO", "--X-X-XOO = X WINS"),
    ("XXOXO-O--", "XXOXO-O-- = O WINS"),
    ("XOXXOOOXX", "XOXXOOOXX = TIE"),
    ("---------", "--------- = TIE"),
    ("XO--XO--X", "XO--XO--X = X WINS"),
    ("OX--OX--O", "OX--OX--O = O WINS"),
    ("XXO---O-X", "XXO---O-X = TIE"),
]

@pytest.mark.parametrize("inp, output", TEST_TIC_TAC_TOE)
def test_tic_tac_toe(inp, output):
    assert " ".join(Winner(inp)) == output