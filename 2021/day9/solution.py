from dataclasses import dataclass
from typing import Union

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Point:
    row_index: int
    col_index: int


class HeightMap:
    _RISK_CONSTANT = 1

    def __init__(self, heights: tuple[tuple[int]]):
        self._heights = heights

        self._local_minima: list[Point] = []

    def calculate_risk_level(self) -> int:
        risk = 0
        for point in self.local_minima:
            risk += self._RISK_CONSTANT + self.get_height(
                point.row_index, point.col_index
            )

        return risk

    @property
    def local_minima(self) -> list[Point]:
        if self._local_minima:
            return self._local_minima

        for row_index, row in enumerate(self._heights):
            for col_index in range(len(row)):
                if self._is_point_local_minimum(row_index, col_index):
                    self._local_minima.append(Point(row_index, col_index))

        return self._local_minima

    def _is_point_local_minimum(self, row_index: int, col_index: int) -> bool:
        up = self.get_height(row_index - 1, col_index)
        down = self.get_height(row_index + 1, col_index)
        left = self.get_height(row_index, col_index - 1)
        right = self.get_height(row_index, col_index + 1)
        height = self.get_height(row_index, col_index)

        return height < up and height < down and height < left and height < right

    def get_height(self, row_index, col_index) -> Union[int, float]:
        if row_index < 0 or col_index < 0:
            return float("inf")

        try:
            return self._heights[row_index][col_index]
        except IndexError:
            return float("inf")


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) for v in x)

    def part1(self):
        height_map = HeightMap(self.input_data[:])
        return height_map.calculate_risk_level()

    def part2(self):
        return None
