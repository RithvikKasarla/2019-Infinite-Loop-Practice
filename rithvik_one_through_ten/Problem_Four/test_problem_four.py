import pytest
import problem_four as p4

game = (("RPPPPPPPRP","PAPER"),
        ("RRRRRPPPPPSSSS", "NO WINNER"),
        ("R", "ROCK"),
        ("S", "SCISSORS"),
        ("P", "PAPER"),
        ("SSSSSSSSP","NO WINNER"))

@pytest.mark.parameterize("Choice, answers", game)
def test_winner(Choice, answer):
    assert(p4.winner(Choice)) == answer