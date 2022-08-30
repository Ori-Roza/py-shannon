import pytest
from shannon import LettersTable
from shannon.src.utils.exceptions import WrongSumOfProbabilities


def test_create_table():
    proba_table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,
    }
    assert proba_table == LettersTable.create("test#").get_raw_table()


def test_wrong_probabilities():
    proba_table = {
        "t": 0.1,
        "e": 0.1,
        "s": 0.1,
        "#": 0.1,
    }
    with pytest.raises(WrongSumOfProbabilities):
        LettersTable(proba_table)


def test_get_letters_list():
    proba_table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,
    }
    assert LettersTable(proba_table).get_letters_list() == ["t", "e", "s", "#"]
