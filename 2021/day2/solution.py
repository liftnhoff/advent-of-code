import enum
import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


class Direction(enum.Enum):
    UP = 0
    DOWN = 1
    FORWARD = 2

    @classmethod
    def from_string(cls, value):
        lookup = {
            "up": cls.UP,
            "down": cls.DOWN,
            "forward": cls.FORWARD,
        }
        direction = lookup.get(value)
        if direction is None:
            raise ValueError(f"'{value}' is not a valid Direction.")

        return direction


@dataclass
class DirectionCommand:
    direction: Direction
    amount: int


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(line):
            if match := re.match(r"(\w+) (\d+)", line):
                direction_commmand = DirectionCommand(
                    Direction.from_string(match.group(1)),
                    int(match.group(2)),
                )
            return direction_commmand

        return parser

    def part1(self):
        x_pos = 0
        depth = 0
        for cmd in self.input_data:
            if cmd.direction is Direction.UP:
                depth -= cmd.amount
            elif cmd.direction is Direction.DOWN:
                depth += cmd.amount
            elif cmd.direction is Direction.FORWARD:
                x_pos += cmd.amount

        return x_pos * depth

    def part2(self):
        x_pos = 0
        depth = 0
        aim = 0
        for cmd in self.input_data:
            if cmd.direction is Direction.UP:
                aim -= cmd.amount
            elif cmd.direction is Direction.DOWN:
                aim += cmd.amount
            elif cmd.direction is Direction.FORWARD:
                x_pos += cmd.amount
                depth += aim * cmd.amount

        return x_pos * depth
