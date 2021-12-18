from dataclasses import dataclass
from typing import Generic, TypeVar, Union

from base.solution import AdventOfCodeSolutionBase

PointType = TypeVar("PointType")


@dataclass
class Point(Generic[PointType]):
    row_index: int
    col_index: int

    def up(self) -> PointType:
        return Point(self.row_index - 1, self.col_index)

    def down(self) -> PointType:
        return Point(self.row_index + 1, self.col_index)

    def left(self) -> PointType:
        return Point(self.row_index, self.col_index - 1)

    def right(self) -> PointType:
        return Point(self.row_index, self.col_index + 1)


class HeightMap:
    _RISK_CONSTANT = 1

    def __init__(self, heights: tuple[tuple[int]]):
        self._heights = heights

        self._local_minima: list[Point] = []

    def calculate_risk_level(self) -> int:
        risk = 0
        for point in self.local_minima:
            risk += self._RISK_CONSTANT + self.get_height(point)

        return risk

    @property
    def local_minima(self) -> list[Point]:
        if self._local_minima:
            return self._local_minima

        for row_index, row in enumerate(self._heights):
            for col_index in range(len(row)):
                point = Point(row_index, col_index)
                if self._is_point_local_minimum(point):
                    self._local_minima.append(point)

        return self._local_minima

    def _is_point_local_minimum(self, point: PointType) -> bool:
        up = self.get_height(point.up())
        down = self.get_height(point.down())
        left = self.get_height(point.left())
        right = self.get_height(point.right())
        height = self.get_height(point)

        return height < up and height < down and height < left and height < right

    def get_height(self, point: PointType) -> Union[int, float]:
        if (
            point.row_index < 0
            or point.row_index >= len(self._heights)
            or point.col_index < 0
            or point.col_index >= len(self._heights[0])
        ):
            return float("inf")
        else:
            return self._heights[point.row_index][point.col_index]


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) for v in x)

    def part1(self):
        height_map = HeightMap(self.input_data[:])
        return height_map.calculate_risk_level()

    def part2(self):
        return None
