from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result = [3, 3]
    assert split_integer(6, 2) == result


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result_of_test = split_integer(8, 1)
    assert result_of_test == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_of_test = split_integer(17, 4)
    assert result_of_test == sorted(result_of_test)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]
    assert sum(result) == 32
    assert len(result) == 6
    assert max(result) - min(result) <= 1
