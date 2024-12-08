from collections import defaultdict
from itertools import combinations, count

from aocli import find_dimensions_2d, read, to_lines

print("--- Day 8: Resonant Collinearity ---")

# read the input data from `input.txt`
data = to_lines(read("input.txt"))

# find the dimensions of the grid
max_i, max_j = find_dimensions_2d(data)

# get the antennas per frequency
frequency_to_antennas = defaultdict(set)
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c.isalnum():
            frequency_to_antennas[c].add((i, j))


def get_unique_antinode_locations(
    resonant_harmonics: bool = False,
) -> set[tuple[int, int]]:
    """Get unique antinode locations for the various frequency-specific antennas."""
    antinodes = set()
    for antennas in frequency_to_antennas.values():
        for antenna_1, antenna_2 in combinations(antennas, 2):
            di, dj = antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]

            for m in count() if resonant_harmonics else (1,):
                if (
                    0 <= (i_1 := antenna_1[0] - di * m) <= max_i - 1
                    and 0 <= (j_1 := antenna_1[1] - dj * m) <= max_j - 1
                ):
                    antinodes.add((i_1, j_1))
                else:
                    break

            for m in count() if resonant_harmonics else (1,):
                if (
                    0 <= (i_2 := antenna_2[0] + di * m) <= max_i - 1
                    and 0 <= (j_2 := antenna_2[1] + dj * m) <= max_j - 1
                ):
                    antinodes.add((i_2, j_2))
                else:
                    break

    return antinodes


# part one
print("--- Part One ---")
print(len(get_unique_antinode_locations()))

# part two
print("--- Part Two ---")
print(len(get_unique_antinode_locations(resonant_harmonics=True)))
