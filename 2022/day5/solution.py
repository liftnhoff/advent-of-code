import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


@dataclass
class CraneInstruction:
    crate_count: int
    source_bin: int
    destination_bin: int


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        # stacks = self._build_crate_stacks()
        # instructions = self._get_instructions()

        return None

    def _build_crate_stacks(self) -> dict[int, list[str]]:
        pattern = re.compile(r"^ 1")
        for line in self.input_data:
            if pattern.search(line):
                bins = [int(v) for v in re.split(r" +", line) if v]

        pattern = re.compile(r"^ *\[")
        stacks = {b: [] for b in bins}
        line_indices = [(b - 1) * 4 + 1 for b in bins]
        for line in reversed(self.input_data):
            if pattern.search(line):
                for bin_index, line_index in zip(bins, line_indices):
                    try:
                        crate = line[line_index]
                        if crate != " ":
                            stacks[bin_index].append(crate)
                    except IndexError:
                        break

        return stacks

    def _get_instructions(self) -> list[CraneInstruction]:
        pattern = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
        instructions = []
        for line in self.input_data:
            if match := pattern.match(line):
                instructions.append(
                    CraneInstruction(
                        int(match.group(1)),
                        int(match.group(2)),
                        int(match.group(3)),
                    )
                )
        print(instructions)
        return instructions

    def part2(self):
        return None
