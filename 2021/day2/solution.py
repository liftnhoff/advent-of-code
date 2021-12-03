import dataclasses
import enum
import re

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

@dataclasses.dataclass
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
        print(self.input_data)
        return

    def part2(self):
        return
