from collections.abc import Callable, Iterable
from itertools import product
from operator import add, mul

from aocli import read, to_lines

print("--- Day 7: Bridge Repair ---")

# read the input data from `input.txt`
data = []
for line in to_lines(read("input.txt")):
    test_value, equation_numbers_str = line.split(": ", maxsplit=1)
    data.append((int(test_value), list(map(int, equation_numbers_str.split(" ")))))


def can_be_made_true(
    test_value: int,
    equation_numbers: list[int],
    operators: Iterable[Callable[[int, int], int]] = (add, mul),
) -> bool:
    """Checks whether an equation can be made true."""
    operator_combinations = product(operators, repeat=len(equation_numbers) - 1)
    for operator_combination in operator_combinations:
        value = equation_numbers[0]
        for other_value, operator in zip(
            equation_numbers[1:], operator_combination, strict=False
        ):
            value = operator(value, other_value)

        if value == test_value:
            return True

    return False


# part one
print("--- Part One ---")
print(
    sum(
        test_value
        for test_value, equation_numbers in data
        if can_be_made_true(test_value, equation_numbers)
    )
)

# part two
print("--- Part Two ---")
print(
    sum(
        test_value
        for test_value, equation_numbers in data
        if can_be_made_true(
            test_value,
            equation_numbers,
            operators=(add, mul, lambda x, y: int("".join(map(str, [x, y])))),
        )
    )
)
