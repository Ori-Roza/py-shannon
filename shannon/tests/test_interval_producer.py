from shannon import LettersTable, ProbaIntervals


def like(first_seq: list, second_seq: list):
    first_flatten = [item for sublist in first_seq for item in sublist]
    second_flatten = [item for sublist in second_seq for item in sublist]
    for i in range(0, len(first_flatten)):
        if abs(first_flatten[i] - second_flatten[i]) > 0.001:
            return False
    return True


def test_get_init_intervals():
    plain = "test#"
    result = {'t': (0, 0.4),
              'e': (0.4, 0.6),
              's': (0.6, 0.8),
              '#': (0.8, 1.0)}

    proba_table = LettersTable.create(plain)
    interval_object = ProbaIntervals(proba_table)
    assert like(interval_object.get_all_proba_intervals().values(), result.values())


def test_apply_first_interval():
    plain = "test#"
    result = (0, 0.4)
    proba_table = LettersTable.create(plain)
    interval_object = ProbaIntervals(proba_table)
    current_interval = interval_object.calc_new_interval("t")
    assert current_interval == result


def test_apply_chain_of_intervals():
    plain = "test#"
    result = [(0, 0.4),
              (0.16, 0.24),
              (0.208, 0.224)]
    proba_table = LettersTable.create(plain)
    interval_object = ProbaIntervals(proba_table)
    first_interval = interval_object.calc_new_interval("t")
    second_interval = interval_object.calc_new_interval("e", "t", first_interval)
    third_interval = interval_object.calc_new_interval("s", "e", second_interval)

    assert like([first_interval, second_interval, third_interval], result)
