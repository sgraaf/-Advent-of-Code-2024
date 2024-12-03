import re
from operator import mul

from aocli import read

print("--- Day 3: Mull It Over ---")

# read the input data from `input.txt`
data = read("input.txt")

# part one
print("--- Part One ---")
sum_real_muls = lambda s: sum(
    mul(*map(int, number_pair))
    for number_pair in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", s)
)
print(sum_real_muls(data))

# part two
print("--- Part Two ---")
print(
    sum_real_muls(re.sub(r"(don't\(\).*?)(?=(?:do\(\)|$))", "", data, flags=re.DOTALL))
)
