from itertools import pairwise

from aocli import read, to_lines

print("--- Day 2: Red-Nosed Reports ---")

# read the input data from `input.txt`
data = [tuple(map(int, line.split(" "))) for line in to_lines(read("input.txt"))]

# part one
print("--- Part One ---")
is_all_increasing = lambda line: all(l < r for l, r in pairwise(line))
is_all_decreasing = lambda line: all(l > r for l, r in pairwise(line))
all_adjacent_levels_within_range = lambda line: all(
    1 <= abs(l - r) <= 3 for l, r in pairwise(line)
)

print(
    sum(
        (is_all_decreasing(line) or is_all_increasing(line))
        and all_adjacent_levels_within_range(line)
        for line in data
    )
)

# part two
print("--- Part Two ---")
create_variants = lambda line: (line[:i] + line[i + 1 :] for i in range(len(line)))

print(
    sum(
        any(
            (is_all_decreasing(line_variant) or is_all_increasing(line_variant))
            and all_adjacent_levels_within_range(line_variant)
            for line_variant in create_variants(line)
        )
        for line in data
    )
)
