from dataclasses import dataclass
from typing import Collection

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Point:
    row_index: int
    column_index: int

    def __hash__(self):
        return hash((self.row_index, self.column_index))


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) for v in x)

    def part1(self):
        visible_tree_points = set()
        for row_index, row in enumerate(self.input_data):
            column_indices = self._locate_visible_trees_in_line_of_sight(row)
            for column_index in column_indices:
                visible_tree_points.add(Point(row_index, column_index))

            last_column_index = len(row) - 1
            column_indices = self._locate_visible_trees_in_line_of_sight(
                tuple(reversed(row))
            )
            for column_index in column_indices:
                visible_tree_points.add(
                    Point(row_index, last_column_index - column_index)
                )

        for column_index, column in enumerate(self._column_wise_map):
            row_indices = self._locate_visible_trees_in_line_of_sight(column)
            for row_index in row_indices:
                visible_tree_points.add(Point(row_index, column_index))

            last_row_index = len(column) - 1
            row_indices = self._locate_visible_trees_in_line_of_sight(
                tuple(reversed(column))
            )
            for row_index in row_indices:
                visible_tree_points.add(Point(last_row_index - row_index, column_index))

        return len(visible_tree_points)

    def _locate_visible_trees_in_line_of_sight(
        self, sight_line: Collection[int]
    ) -> list[int]:
        tallest_height = -1
        visible_tree_indices = []
        for index, tree_height in enumerate(sight_line):
            if tree_height > tallest_height:
                visible_tree_indices.append(index)
                tallest_height = tree_height

        return visible_tree_indices

    @property
    def _column_wise_map(self) -> list[list[int]]:
        column_wise_map = list(
            list([0] * len(self.input_data)) for _ in range(len(self.input_data[0]))
        )
        for row_index, row in enumerate(self.input_data):
            for column_index, value in enumerate(row):
                column_wise_map[column_index][row_index] = value

        return column_wise_map

    def part2(self):
        # for row_index, row in enumerate(self.input_data):
        #     for column_index, value in enumerate(row):

        return None
