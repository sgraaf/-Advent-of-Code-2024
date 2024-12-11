from typing import Literal

from aocli import find_dimensions_2d, find_neighbouring_indices_2d, read, to_lines

print("--- Day 10: Hoof It ---")

# read the input data from `input.txt`
data = [list(map(int, line)) for line in to_lines(read("input.txt"))]
max_i, max_j = find_dimensions_2d(data)


def measure_trail(
    trail: tuple[tuple[int, int], ...],
    measure: Literal["score", "rating"],
    seen: set | None = None,
) -> int:
    """Measure a trail, either by its score or by its rating."""
    if seen is None:
        seen = set()

    last_i, last_j = trail[-1]
    for neighbour_i, neighbour_j in find_neighbouring_indices_2d(
        last_i, last_j, (0, max_i), (0, max_j)
    ):
        if (neighbour_i, neighbour_j) not in trail and (
            neighbour_val := data[neighbour_i][neighbour_j]
        ) - data[last_i][last_j] == 1:
            neighbour_trail = (*trail, (neighbour_i, neighbour_j))
            if neighbour_val == 9:
                seen.add(
                    neighbour_trail
                    if measure == "rating"
                    else (neighbour_i, neighbour_j)
                )
            else:
                measure_trail(neighbour_trail, measure, seen)

    return len(seen)


# part one
print("--- Part One ---")
print(
    sum(
        measure_trail(((i, j),), "score")
        for i, line in enumerate(data)
        for j, c in enumerate(line)
        if c == 0
    )
)

# part two
print("--- Part Two ---")
print(
    sum(
        measure_trail(((i, j),), "rating")
        for i, line in enumerate(data)
        for j, c in enumerate(line)
        if c == 0
    )
)
