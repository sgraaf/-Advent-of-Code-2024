from collections import defaultdict
from collections.abc import Sequence
from itertools import filterfalse

from aocli import read

print("--- Day 5: Print Queue ---")

# read the input data from `input.txt`
page_ordering_rules_str, updates_str = read("input.txt").split("\n\n", maxsplit=1)

# parse the page ordering rules
page_ordering_rules: dict[int, set[int]] = defaultdict(set)
for page_ordering_rule in page_ordering_rules_str.splitlines():
    x, y = map(int, page_ordering_rule.split("|", maxsplit=1))
    page_ordering_rules[x].add(y)

# parse the updates
updates = [list(map(int, update.split(","))) for update in updates_str.splitlines()]


def is_correctly_ordered(update: Sequence[int]) -> bool:
    """Determines whether an update is correctly ordered (or not)."""
    for page_number_idx, page_number in enumerate(update):
        if not set(update[page_number_idx + 1 :]) <= page_ordering_rules[page_number]:
            return False
    return True


def order(update: list[int]) -> list[int]:
    """Orders an incorrectly ordered update."""
    page_num_to_number_of_after_pages = {}
    for page_num_idx, page_num in enumerate(update):
        rest_of_update = update[:page_num_idx] + update[page_num_idx + 1 :]
        page_num_to_number_of_after_pages[page_num] = len(
            page_ordering_rules[page_num] & set(rest_of_update)
        )
    return sorted(update, key=page_num_to_number_of_after_pages.get, reverse=True)


# part one
print("--- Part One ---")
print(sum(update[len(update) // 2] for update in filter(is_correctly_ordered, updates)))

# part two
print("--- Part Two ---")
print(
    sum(
        update[len(update) // 2]
        for update in map(order, filterfalse(is_correctly_ordered, updates))
    )
)
