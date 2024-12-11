from collections import defaultdict

import tqdm

from base.solution import AdventOfCodeSolutionBase


class Stone:
    def __init__(self, value):
        self.value = value

    def blink_action(self):
        if self.value == 0:
            self.value = 1
            return None

        value_str = str(self.value)
        if len(value_str) % 2 == 0:
            self.value = int(value_str[: len(value_str) // 2])
            return Stone(int(value_str[len(value_str) // 2 :]))

        self.value *= 2024

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        stones = list(Stone(int(v)) for v in self.input_data[0].split())
        blinks = 25
        for blink in tqdm.tqdm(range(blinks), maxinterval=1):
            index = 0
            while index < len(stones):
                new_stone = stones[index].blink_action()
                if new_stone is None:
                    index += 1
                else:
                    stones.insert(index + 1, new_stone)
                    index += 2

        return len(stones)

    def part2(self):
        counts_by_stone = defaultdict(int)
        for stone in list(int(v) for v in self.input_data[0].split()):
            counts_by_stone[stone] += 1

        blinks = 75
        pbar = tqdm.tqdm(range(blinks))
        for blink in pbar:
            new_counts_by_stone = defaultdict(int)
            for stone in tuple(counts_by_stone.keys()):
                count = counts_by_stone.pop(stone)

                if stone == 0:
                    stone = 1
                    new_counts_by_stone[stone] += count
                    continue

                value_str = str(stone)
                if len(value_str) % 2 == 0:
                    stone = int(value_str[: len(value_str) // 2])
                    new_stone = int(value_str[len(value_str) // 2 :])
                    new_counts_by_stone[stone] += count
                    new_counts_by_stone[new_stone] += count
                    continue

                stone *= 2024
                new_counts_by_stone[stone] += count

            counts_by_stone = new_counts_by_stone

            pbar.refresh()

        return sum(v for v in counts_by_stone.values())
