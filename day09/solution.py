from collections.abc import Iterator
from itertools import count

from aocli import read

print("--- Day 9: Disk Fragmenter ---")

# read the input data from `input.txt`
disk_map = read("input.txt").strip()

# un-denseify the disk map
position = 0
disk = {}
for idx in range(0, len(disk_map), 2):
    file_length = int(disk_map[idx])
    for position in range(position, position + file_length):  # noqa: B020
        disk[position] = idx // 2

    if idx + 1 < len(disk_map):
        free_space_length = int(disk_map[idx + 1])
        position += free_space_length + 1

# create a copy of the disk to be used in part 2
disk_backup = disk.copy()


def get_first_free_space_position(disk: dict[int, int], start: int = 0) -> int:
    """Get the first position (on disk) of the first free space."""
    for position in count(start):  # noqa: RET503
        if position not in disk:
            return position


def get_last_file_position(disk: dict[int, int], stop: int = 0) -> int:
    """Get the last position (on disk) of the last file."""
    if not stop:
        stop = max(disk.keys())
    for position in range(stop, -1, -1):  # noqa: RET503
        if position in disk:
            return position


def get_first_position_of_last_file_block(
    disk: dict[int, int], last_file_position: int
) -> int:
    """Get the first position (on disk) of the last file."""
    id_number = disk[last_file_position]
    for position in range(last_file_position - 1, 0, -1):  # noqa: RET503
        if disk.get(position) != id_number:
            return position + 1


def get_free_space_blocks(
    disk: dict[int, int], start: int, stop: int
) -> Iterator[tuple[int, int]]:
    """Yield all free space blocks between the start and stop positions."""
    block_start = None
    block_end = None
    for position in range(start, stop + 1):
        if position not in disk:
            if block_start is None:
                block_start = position
            block_end = position
        elif not (block_start is None or block_end is None):
            yield block_start, block_end
            block_start = None
            block_end = None


# part one
print("--- Part One ---")
first_free_space_position = 0
while (
    first_free_space_position := get_first_free_space_position(
        disk, first_free_space_position
    )
) < (last_file_block_end := max(disk.keys())):
    disk[first_free_space_position] = disk.pop(last_file_block_end)

print(sum(k * v for k, v in disk.items()))

# part two
print("--- Part Two ---")
disk = disk_backup.copy()
first_free_space_position = 0
last_file_block_end = max(disk.keys())
already_moved_blocks = set()
while (
    first_free_space_position := get_first_free_space_position(
        disk, first_free_space_position
    )
) < (last_file_block_end := get_last_file_position(disk, last_file_block_end)):
    last_file_block_start = get_first_position_of_last_file_block(
        disk, last_file_block_end
    )
    last_file_block = tuple(
        disk[position]
        for position in range(last_file_block_start, last_file_block_end + 1)
    )

    if last_file_block not in already_moved_blocks:
        for free_block_start, free_block_end in get_free_space_blocks(
            disk, first_free_space_position, last_file_block_end
        ):
            if (
                last_file_block_end - last_file_block_start + 1
                <= free_block_end - free_block_start + 1
            ):
                for block_position in range(len(last_file_block)):
                    disk[free_block_start + block_position] = disk.pop(
                        last_file_block_end - block_position
                    )
                break

        last_file_block_end = last_file_block_start - 1

print(sum(k * v for k, v in disk.items()))
