import pytest as pyt
import problem_two as p1

def test_if_code_quest_is_fun():
    assert p1.AEIOU("code quest is fun") == "6"

def test_if_try_two():
    assert  p1.AEIOU("queueing has five vowels in a row") == "8"

def test_if_five_voels():
    assert  p1.AEIOU("queueing has five vowels in a row") == "13"