from collections.abc import Sequence
from typing import TypeVar

from aocli import find_dimensions_2d, read, to_lines

print("--- Day 4: Ceres Search ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

T = TypeVar("T")


def find_neighbours_in_all_directions_2d(
    grid: Sequence[Sequence[T]], i: int, j: int, n: int = 1
) -> list[list[T]]:
    max_i, max_j = find_dimensions_2d(grid)
    neighbours = []
    for di, dj in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]:
        if 0 <= i + di * n < max_i and 0 <= j + dj * n < max_j:
            neighbour = []
            for n_ in range(1, n + 1):
                i_ = i + di * n_
                j_ = j + dj * n_
                neighbour.append(data[i_][j_])
            neighbours.append(neighbour)
    return neighbours


# part one
print("--- Part One ---")
max_i, max_j = find_dimensions_2d(data)
xmas_count = 0
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == "X":
            xmas_count += list(
                map("".join, find_neighbours_in_all_directions_2d(data, i, j, 3))
            ).count("MAS")
print(xmas_count)

# part two
print("--- Part Two ---")
x_mas_count = 0
for i in range(1, max_i - 1):
    for j in range(1, max_j - 1):
        if (
            data[i][j] == "A"
            and (data[i - 1][j - 1], data[i + 1][j + 1]) in {("M", "S"), ("S", "M")}
            and (data[i - 1][j + 1], data[i + 1][j - 1]) in {("M", "S"), ("S", "M")}
        ):
            x_mas_count += 1
print(x_mas_count)
