__author__ = "Ori Roza"

import typing

LettersTable = typing.TypeVar("LettersTable")


def calc_interval(current_interval, prev_interval) -> typing.Tuple[float, float]:
    start_interval = prev_interval[0] + current_interval[0] * (prev_interval[1] - prev_interval[0])
    current_letter_proba = current_interval[1] - current_interval[0]
    end_interval = start_interval + (prev_interval[1] - prev_interval[0]) * current_letter_proba

    return start_interval, end_interval


class ProbaIntervals:
    def __init__(self, probabilities_table: LettersTable):
        self.__probabilities_table = probabilities_table
        self.__proba_intervals = self.build_initial_intervals()

    def build_initial_intervals(self) -> typing.Dict[str, typing.Tuple[float, float]]:
        intervals = []
        proba_table = self.__probabilities_table.get_raw_table()
        starting_point = 0
        for letter in proba_table:
            proba = proba_table.get(letter)
            intervals.append((starting_point, starting_point + proba))
            starting_point = starting_point + proba
        return dict(zip(proba_table.keys(), intervals))

    def get_proba_interval(self, letter) -> typing.Tuple[float, float]:
        if letter in self.__proba_intervals:
            return self.__proba_intervals[letter]

    def get_all_proba_intervals(self) -> typing.Dict[str, typing.Tuple[float, float]]:
        return self.__proba_intervals

    def calc_new_interval(self, letter, prev_letter=None, previous_interval=None) -> typing.Tuple[float, float]:
        letter_range = self.get_proba_interval(letter)
        if not prev_letter:
            start_limit, end_limit = letter_range[0], letter_range[1]
        else:
            start_limit, end_limit = calc_interval(letter_range, previous_interval)
        return start_limit, end_limit
