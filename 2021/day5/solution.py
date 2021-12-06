import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class VentLine:
    x1: int
    y1: int
    x2: int
    y2: int


class VentMap:
    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y
        self.grid = [[0] * max_x for _ in range(max_y)]

    def add_vent(self, vent_line: VentLine):
        pass


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(line: str):
            if match := re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line):
                return VentLine(
                    int(match.group(1)),
                    int(match.group(2)),
                    int(match.group(3)),
                    int(match.group(4)),
                )

        return parser

    def part1(self):
        vent_map = self._initialize_map()
        for row in vent_map.grid:
            print(row)
        return None

    def _initialize_map(self) -> VentMap:
        max_x = 0
        max_y = 0
        for vent_line in self.input_data:
            if vent_line.x1 > max_x:
                max_x = vent_line.x1
            if vent_line.x2 > max_x:
                max_x = vent_line.x2

            if vent_line.y1 > max_y:
                max_y = vent_line.y1
            if vent_line.y2 > max_y:
                max_y = vent_line.y2

        return VentMap(max_x, max_y)

    def part2(self):
        return None
