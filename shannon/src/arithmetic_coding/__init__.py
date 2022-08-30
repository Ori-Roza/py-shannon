__author__ = "Ori Roza"

from random import uniform
from shannon.src.letters_table import LettersTable
from shannon.src.interval_producer import ProbaIntervals
from shannon.src.utils.exceptions import TerminatorDoesNotExists


class ArithmeticCoding:
    def __init__(self, probabilities_table: LettersTable, terminator: str = "#"):
        self.__terminator = terminator
        self.__probabilities_table = probabilities_table

        if not self.__probabilities_table.letter_exists(self.__terminator):
            raise TerminatorDoesNotExists(f"terminator {self.__terminator} does not exist in probabilities table")

        self.__range_obj = ProbaIntervals(self.__probabilities_table)

    @property
    def terminator(self) -> str:
        return self.__terminator

    @property
    def proba_table(self) -> LettersTable:
        return self.__probabilities_table

    @property
    def interval(self) -> ProbaIntervals:
        return self.__range_obj

    def encrypt(self, word: str) -> float:
        """
        
        :param word:
        :return:
        """
        current_interval = None

        if self.terminator not in word:
            raise TerminatorDoesNotExists("There is no terminator {} in ")

        for index, letter in enumerate(word):
            if not self.proba_table.letter_exists(letter):
                raise ValueError(f"letter {letter} does not exists in probabilities table!")
            if index == 0:
                current_interval = self.interval.calc_new_interval(letter)
            else:
                prev_letter = word[index - 1]
                current_interval = self.interval.calc_new_interval(letter, prev_letter, current_interval)
            print(f"interval {current_interval}")

        return uniform(current_interval[0], current_interval[1])

    def decrypt(self, cipher: float) -> str:
        """

        :param cipher:
        :return:
        """
        plain = ""
        prev_interval = None
        last_letter = ""

        proba_table = self.interval.get_all_proba_intervals()

        # continue with the rest
        while self.terminator not in plain:
            for letter, interval in proba_table.items():
                if prev_interval is None:
                    # gets init interval
                    _interval = interval
                else:
                    _interval = self.interval.calc_new_interval(letter, last_letter, prev_interval)
                if _interval[0] <= cipher <= _interval[1]:
                    plain += letter
                    last_letter = letter
                    prev_interval = _interval
                    if letter == self.terminator:
                        return plain


if __name__ == '__main__':
    table = {
        "t": 0.4,
        "e": 0.2,
        "s": 0.2,
        "#": 0.2,  # terminator
    }
    my_table = LettersTable.create("test#")
    assert my_table.get_raw_table() == table
    ac = ArithmeticCoding(LettersTable(table))
    cipher = ac.encrypt("test#")
    plain = ac.decrypt(cipher)
    print(cipher)
    print(plain)
