from aocli import read, to_lines

print("--- Day 1: Historian Hysteria ---")

# read the input data from `input.txt`
data = [tuple(map(int, line.split("   "))) for line in to_lines(read("input.txt"))]

# part one
print("--- Part One ---")
left, right = zip(*data, strict=False)
total_distance = sum(
    abs(l - r) for l, r in zip(sorted(left), sorted(right), strict=False)
)
print(total_distance)

# part two
print("--- Part Two ---")
similarity_score = sum(l * right.count(l) for l in left)
print(similarity_score)
