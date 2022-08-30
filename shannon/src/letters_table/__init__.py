from __future__ import annotations

__author__ = "Ori Roza"

import typing
from collections import Counter

from shannon.src.utils.exceptions import WrongSumOfProbabilities


class LettersTable:
    def __init__(self, probabilities_table: typing.Dict[str, float]):
        self.__table = probabilities_table
        if not self.check_probabilities():
            raise WrongSumOfProbabilities("sum of probabilities is not 1")

        self.__letters = list(self.get_raw_table().keys())

    def check_probabilities(self):
        return sum([self.get_raw_table()[letter] for letter in self.get_raw_table()]) == 1

    def get_raw_table(self) -> typing.Dict[str, float]:
        return self.__table

    def get_letters_list(self) -> typing.List[str]:
        return self.__letters

    def get_letter_index(self, letter: str) -> int:
        if self.letter_exists(letter):
            return self.get_letters_list().index(letter)
        return -1

    def letter_exists(self, letter: str) -> bool:
        return letter in self.get_letters_list()

    @classmethod
    def create(cls, text: str) -> LettersTable:
        current_table = {}
        text_size = len(text)
        counter = Counter(text)

        for letter, freq in counter.items():
            current_table[letter] = freq / text_size

        return cls(current_table)
