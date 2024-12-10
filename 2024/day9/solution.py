from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        disk = []
        for index, size_str in enumerate(self.input_data[0]):
            size = int(size_str)
            if index % 2 == 0:
                disk.extend([index // 2] * size)
            else:
                disk.extend(["."] * size)

        index = -1
        while index < len(disk) - 1:
            index += 1
            if disk[index] != ".":
                continue

            while True:
                block_id = disk.pop()
                if block_id != ".":
                    break

            if disk.index("."):
                disk[index] = block_id
            else:
                disk.append(block_id)
                break

        checksum = 0
        for index, block_id in enumerate(disk):
            checksum += index * block_id

        return checksum

    def part2(self):
        disk = []
        for index, size_str in enumerate(self.input_data[0]):
            size = int(size_str)
            if index % 2 == 0:
                disk.append(BlockRange(index // 2, size))
            else:
                disk.append(BlockRange(FREE_SPACE_ID, size))

        bi = len(disk)
        while bi > 0:
            bi -= 1
            block_range = disk[bi]
            # disk_str = "".join(
            #     str(br.block_id) * br.size
            #     if br.block_id != FREE_SPACE_ID
            #     else "." * br.size
            #     for br in disk
            # )
            # print(disk_str)
            if block_range.block_id == FREE_SPACE_ID:
                continue

            index = -1
            found_space = False
            while index < bi:
                index += 1
                free_range = disk[index]
                if free_range.block_id != FREE_SPACE_ID:
                    continue
                if block_range.size <= free_range.size:
                    found_space = True
                    break

            if found_space:
                free_range = disk[index]
                if free_range.size == block_range.size:
                    disk[index] = block_range
                    disk[bi] = free_range
                else:
                    new_free_size = free_range.size - block_range.size
                    disk[index] = block_range
                    disk[bi] = BlockRange(FREE_SPACE_ID, block_range.size)
                    disk.insert(index + 1, BlockRange(FREE_SPACE_ID, new_free_size))

        new_disk = []
        for block_range in disk:
            new_disk.extend([block_range.block_id] * block_range.size)

        checksum = 0
        for index, block_id in enumerate(new_disk):
            if block_id != FREE_SPACE_ID:
                checksum += index * block_id

        return checksum


@dataclass
class BlockRange:
    block_id: int
    size: int


FREE_SPACE_ID = -1
