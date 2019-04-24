import pytest
import problem_four as p4

Game = (("RPPPPPPPRP","PAPER"),
        ("RRRRRPPPPPSSSS", "NO WINNER"),
        ("R", "ROCK"),
        ("S", "SCISSORS"),
        ("P", "PAPER"),
        ("SSSSSSSSP","NO WINNER"))

@pytest.mark.parameterize("Choice, Answers", Game)
def test_winner(Choice, Answer):
    assert(p4.winner(Choice)) == Answer