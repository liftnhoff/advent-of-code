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
        self.grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    def __str__(self):
        grid_values = ["VentMap"]
        for row in self.grid:
            grid_values.append("".join(f"{v: 3d}" for v in row))

        return "\n".join(grid_values)

    def add_vent(self, vent_line: VentLine):
        if vent_line.x1 == vent_line.x2:
            self._add_vertical_vent(vent_line)
        elif vent_line.y1 == vent_line.y2:
            self._add_horizontal_vent(vent_line)
        else:
            pass  # Skip diagonal lines.

    def _add_vertical_vent(self, vent_line):
        y_values = sorted([vent_line.y1, vent_line.y2])
        for y_value in range(y_values[0], y_values[1] + 1):
            self.grid[y_value][vent_line.x1] += 1

    def _add_horizontal_vent(self, vent_line):
        x_values = sorted([vent_line.x1, vent_line.x2])
        for x_value in range(x_values[0], x_values[1] + 1):
            self.grid[vent_line.y1][x_value] += 1


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
        for vent_line in self.input_data:
            vent_map.add_vent(vent_line)
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
