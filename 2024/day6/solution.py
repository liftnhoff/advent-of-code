from dataclasses import dataclass
from enum import Enum

from base.solution import AdventOfCodeSolutionBase


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


@dataclass
class GuardPosition:
    ri: int
    ci: int
    facing: Direction

    def next_forward_position(self):
        if self.facing is Direction.UP:
            return GuardPosition(self.ri - 1, self.ci, self.facing)
        elif self.facing is Direction.DOWN:
            return GuardPosition(self.ri + 1, self.ci, self.facing)
        elif self.facing is Direction.LEFT:
            return GuardPosition(self.ri, self.ci - 1, self.facing)
        elif self.facing is Direction.RIGHT:
            return GuardPosition(self.ri, self.ci + 1, self.facing)

    def turn_right_position(self):
        if self.facing is Direction.UP:
            return GuardPosition(self.ri, self.ci, Direction.RIGHT)
        elif self.facing is Direction.DOWN:
            return GuardPosition(self.ri, self.ci, Direction.LEFT)
        elif self.facing is Direction.LEFT:
            return GuardPosition(self.ri, self.ci, Direction.UP)
        elif self.facing is Direction.RIGHT:
            return GuardPosition(self.ri, self.ci, Direction.DOWN)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        positions = [self._get_initial_guard_position()]
        while True:
            next_gp = positions[-1].next_forward_position()
            try:
                grid_value = self.input_data[next_gp.ri][next_gp.ci]
            except IndexError:
                break

            if grid_value == "#":
                positions.append(positions[-1].turn_right_position())
            else:
                positions.append(next_gp)

        return len({(p.ri, p.ci) for p in positions})

    def _get_initial_guard_position(self):
        for ri, row in enumerate(self.input_data):
            for ci, value in enumerate(row):
                if value == "^":
                    return GuardPosition(ri, ci, Direction.UP)

    def part2(self):
        return None
