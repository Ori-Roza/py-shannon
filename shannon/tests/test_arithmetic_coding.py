import pytest
from shannon import ArithmeticCoding, LettersTable
from shannon.src.utils.exceptions import TerminatorDoesNotExists


def test_encrypt():
    plain = "test#"
    result = 0.2143443503590491
    proba_table = LettersTable.create(plain)
    coder = ArithmeticCoding(proba_table)
    assert abs(coder.encrypt(plain) - result) < 0.01


def test_decrypt():
    cipher = 0.21317984366576836
    proba_table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,  # terminator
    }
    result = "test#"
    proba_table = LettersTable(proba_table)
    coder = ArithmeticCoding(proba_table)
    assert coder.decrypt(cipher) == result


def test_no_terminator():
    proba_table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,
    }
    proba_table = LettersTable(proba_table)
    with pytest.raises(TerminatorDoesNotExists):
        ArithmeticCoding(proba_table, "r")


def test_letter_not_found():
    proba_table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,
    }
    proba_table = LettersTable(proba_table)
    with pytest.raises(ValueError):
        ArithmeticCoding(proba_table).encrypt("test1#")
