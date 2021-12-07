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
    def __init__(self, x_length: int, y_length: int):
        self.grid = [[0] * x_length for _ in range(y_length)]

    def __str__(self):
        grid_values = ["VentMap"]
        for row in self.grid:
            grid_values.append("".join(f"{v: 2d}" for v in row))

        return "\n".join(grid_values)

    def add_vent(self, vent_line: VentLine, include_diagonal: bool = False):
        if vent_line.x1 == vent_line.x2:
            self._add_vertical_vent(vent_line)
        elif vent_line.y1 == vent_line.y2:
            self._add_horizontal_vent(vent_line)
        else:
            if include_diagonal:
                self._add_diagonal_vent(vent_line)

    def _add_vertical_vent(self, vent_line: VentLine):
        y_indexes = sorted([vent_line.y1, vent_line.y2])
        for y_value in range(y_indexes[0], y_indexes[1] + 1):
            self.grid[y_value][vent_line.x1] += 1

    def _add_horizontal_vent(self, vent_line: VentLine):
        x_indexes = sorted([vent_line.x1, vent_line.x2])
        for x_value in range(x_indexes[0], x_indexes[1] + 1):
            self.grid[vent_line.y1][x_value] += 1

    def _add_diagonal_vent(self, vent_line: VentLine):
        # Always start the line at the top-most point.
        points = sorted(
            [(vent_line.x1, vent_line.y1), (vent_line.x2, vent_line.y2)],
            key=lambda v: v[1],
        )
        x_index = points[0][0]
        y_index = points[0][1]
        while y_index <= points[1][1]:
            self.grid[y_index][x_index] += 1
            y_index += 1
            if points[0][0] < points[1][0]:
                x_index += 1  # Diagonal from top left to bottom right.
            else:
                x_index -= 1  # Diagonal from top right to bottom left.

    def count_points_with_multiple_vents(self) -> int:
        count = 0
        for row in self.grid:
            for value in row:
                if value >= 2:
                    count += 1

        return count


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
        vent_map = self._initialize_empty_map()
        for vent_line in self.input_data:
            vent_map.add_vent(vent_line)

        return vent_map.count_points_with_multiple_vents()

    def _initialize_empty_map(self) -> VentMap:
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

        x_length = max_x + 1
        y_length = max_y + 1
        return VentMap(x_length, y_length)

    def part2(self):
        vent_map = self._initialize_empty_map()
        for vent_line in self.input_data:
            vent_map.add_vent(vent_line, include_diagonal=True)

        return vent_map.count_points_with_multiple_vents()
