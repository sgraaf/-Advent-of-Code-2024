from itertools import cycle, product

from aocli import find_dimensions_2d, read, to_lines

print("--- Day 6: Guard Gallivant ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# find the dimensions of the grid
max_i, max_j = find_dimensions_2d(data)

# get the obstructions as a set
obstructions = {
    (i, j) for i, line in enumerate(data) for j, c in enumerate(line) if c == "#"
}

# get the starting position of the guard
i, j = {
    (i, j) for i, line in enumerate(data) for j, c in enumerate(line) if c == "^"
}.pop()

# define the directions
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # up, right, down, left


def predict_path(
    i: int, j: int, new_obstruction: tuple[int, int] | None = None
) -> set[tuple[int, int]]:
    """Predict the path of the guard, returning its distinct positions."""
    distinct_positions_and_directions = set()

    directions_cycle = cycle(directions)
    di, dj = next(directions_cycle)

    new_obstructions = set(obstructions)
    if new_obstruction is not None:
        new_obstructions.add(new_obstruction)

    while 0 <= i <= max_i - 1 and 0 <= j <= max_j - 1:
        if (i, j, (di, dj)) in distinct_positions_and_directions:
            break
        distinct_positions_and_directions.add((i, j, (di, dj)))
        if (next_i := i + di, next_j := j + dj) in new_obstructions:
            di, dj = next(directions_cycle)
        else:
            i, j = next_i, next_j

    else:
        return {(i, j) for i, j, _ in distinct_positions_and_directions}

    msg = "The guard got stuck in a loop."
    raise RuntimeError(msg)


# part one
print("--- Part One ---")
print(len(predict_path(i, j)))

# part two
print("--- Part Two ---")
obstruction_positions = set()
for k, l in product(range(max_i), range(max_j)):
    if (k, l) not in obstructions and (k, l) != (i, j):
        try:
            predict_path(i, j, new_obstruction=(k, l))
        except RuntimeError:
            obstruction_positions.add((k, l))

print(len(obstruction_positions))
