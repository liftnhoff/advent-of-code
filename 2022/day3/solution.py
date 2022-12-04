from base.solution import AdventOfCodeSolutionBase


class Rucksack:
    _PRIORITY_LOOKUP = {
        c: v
        for v, c in enumerate(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1
        )
    }

    def __init__(self, contents: str):
        self.contents = contents

        compartment_count = len(self.contents) // 2
        self.first_compartment = self.contents[:compartment_count]
        self.second_compartment = self.contents[compartment_count:]

    def __repr__(self):
        return f"Rucksack({self.first_compartment} + {self.second_compartment})"

    def items_in_both_compartments(self) -> set[str]:
        return set(self.first_compartment).intersection(set(self.second_compartment))

    @classmethod
    def item_priority(cls, item_letter: str) -> int:
        return cls._PRIORITY_LOOKUP[item_letter]


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: Rucksack(x)

    def part1(self):
        priority_total = 0
        for rucksack in self.input_data:
            priority_total += Rucksack.item_priority(
                rucksack.items_in_both_compartments().pop()
            )
        return priority_total

    def part2(self):
        priority_total = 0
        elf_count = 3
        current_set = None
        for index, rucksack in enumerate(self.input_data):
            if index % elf_count == 0 and current_set:
                priority_total += Rucksack.item_priority(current_set.pop())
                current_set = None

            if current_set is None:
                current_set = set(rucksack.contents)
            else:
                current_set = current_set.intersection(rucksack.contents)

        priority_total += Rucksack.item_priority(current_set.pop())

        return priority_total
