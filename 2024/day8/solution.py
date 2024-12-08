from collections import defaultdict
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Position:
    ri: int
    ci: int

    def __eq__(self, other):
        if self.ri == other.ri and self.ci == other.ci:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.ri, self.ci))


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        pos_by_freq = defaultdict(list)
        for ri, row in enumerate(self.input_data):
            for ci, freq in enumerate(row):
                if freq != ".":
                    pos_by_freq[freq].append(Position(ri, ci))

        antinodes = set()
        for freq, positions in pos_by_freq.items():
            antinodes.update(self._find_antinodes(positions))

        return len(antinodes)

    def _find_antinodes(self, positions: list[Position]) -> set[Position]:
        antinodes = set()
        rmin, rmax = 0, len(self.input_data) - 1
        cmin, cmax = 0, len(self.input_data[0]) - 1
        for index, a_pos in enumerate(positions):
            for b_pos in positions[index:]:
                r_delta = a_pos.ri - b_pos.ri
                c_delta = a_pos.ci - b_pos.ci
                possible_an = (
                    Position(a_pos.ri + r_delta, a_pos.ci + c_delta),
                    Position(a_pos.ri - r_delta, a_pos.ci - c_delta),
                    Position(b_pos.ri + r_delta, b_pos.ci + c_delta),
                    Position(b_pos.ri - r_delta, b_pos.ci - c_delta),
                )
                for an in possible_an:
                    if (
                        an != a_pos
                        and an != b_pos
                        and rmin <= an.ri <= rmax
                        and cmin <= an.ci <= cmax
                    ):
                        antinodes.add(an)

        return antinodes

    def part2(self):
        return None
