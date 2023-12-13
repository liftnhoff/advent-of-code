import itertools
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Position:
    row_index: int
    col_index: int

    def __post_init__(self):
        self.pair_tuple = (self.row_index, self.col_index)

    def __hash__(self):
        return hash(self.pair_tuple)


class ExpandingUniverse:
    def __init__(self, raw_map: tuple[str], expansion_multiple: int = 1):
        self.raw_map = raw_map
        self.expansion_multiple = expansion_multiple

        seen_galaxies = set()
        rows_with_galaxies = set()
        cols_with_galaxies = set()
        for row_index, row in enumerate(self.raw_map):
            for col_index, value in enumerate(row):
                if value == "#":
                    seen_galaxies.add(Position(row_index, col_index))
                    rows_with_galaxies.add(row_index)
                    cols_with_galaxies.add(col_index)

        self.empty_rows = set(range(len(self.raw_map))).difference(rows_with_galaxies)
        self.empty_cols = set(range(len(self.raw_map[0]))).difference(
            cols_with_galaxies
        )
        self.galaxies = tuple(
            sorted(
                sorted(seen_galaxies, key=lambda g: g.col_index),
                key=lambda g: g.row_index,
            )
        )

    def shortest_distance_between_all_galaxies(self) -> list[list[int | None]]:
        distances = [[None] * len(self.galaxies) for _ in self.galaxies]
        for a_index, ga in enumerate(self.galaxies):
            for b_index, gb in enumerate(self.galaxies):
                if b_index <= a_index:
                    continue
                distances[a_index][b_index] = self.distance_between_galaxies(ga, gb)

        return distances

    def distance_between_galaxies(self, ga: Position, gb: Position) -> int:
        row_distance = abs(gb.row_index - ga.row_index)
        min_row = min((gb.row_index, ga.row_index))
        rows_to_check = set(range(min_row, min_row + row_distance))
        row_distance += (self.expansion_multiple - 1) * len(
            rows_to_check.intersection(self.empty_rows)
        )

        col_distance = abs(gb.col_index - ga.col_index)
        min_col = min((gb.col_index, ga.col_index))
        cols_to_check = set(range(min_col, min_col + col_distance))
        col_distance += (self.expansion_multiple - 1) * len(
            cols_to_check.intersection(self.empty_cols)
        )
        return row_distance + col_distance


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        universe = ExpandingUniverse(self.input_data[:], expansion_multiple=2)
        shortest_distances = universe.shortest_distance_between_all_galaxies()
        return sum(x for x in itertools.chain(*shortest_distances) if x is not None)

    def part2(self):
        universe = ExpandingUniverse(self.input_data[:], expansion_multiple=1_000_000)
        shortest_distances = universe.shortest_distance_between_all_galaxies()
        return sum(x for x in itertools.chain(*shortest_distances) if x is not None)
