from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(instruction: str) -> tuple[str, int]:
            direction, amount = instruction.split(" ")
            return direction, int(amount)

        return parser

    def part1(self):
        rope = Rope()
        for direction, amount in self.input_data:
            print(direction, amount)
            if direction == "R":
                rope.move_right(amount)
            elif direction == "L":
                rope.move_left(amount)
            elif direction == "U":
                rope.move_up(amount)
            elif direction == "D":
                rope.move_down(amount)
            else:
                raise RuntimeError(f"Invalid direction: {direction}")

        return len(rope.seen_tail_positions)

    def part2(self):
        return None


class Rope:
    def __init__(self):
        self.head_position = Position(0, 0)
        self.tail_position = Position(0, 0)
        print(self.head_position, self.tail_position)

        self.seen_tail_positions = {self.tail_position}

    def move_right(self, amount: int) -> None:
        for _ in range(amount):
            old_head_position = Position(self.head_position.x, self.head_position.y)
            self.head_position.x += 1
            self._move_tail(old_head_position)

    def move_left(self, amount: int) -> None:
        for _ in range(amount):
            old_head_position = Position(self.head_position.x, self.head_position.y)
            self.head_position.x -= 1
            self._move_tail(old_head_position)

    def move_up(self, amount: int) -> None:
        for _ in range(amount):
            old_head_position = Position(self.head_position.x, self.head_position.y)
            self.head_position.y += 1
            self._move_tail(old_head_position)

    def move_down(self, amount: int) -> None:
        for _ in range(amount):
            old_head_position = Position(self.head_position.x, self.head_position.y)
            self.head_position.y -= 1
            self._move_tail(old_head_position)

    def _move_tail(self, old_head_position) -> None:
        x_delta = self.head_position.x - self.tail_position.x
        y_delta = self.head_position.y - self.tail_position.y
        if abs(x_delta) > 1 or abs(y_delta) > 1:
            self.tail_position = old_head_position
            print(self.head_position, self.tail_position)
            self.seen_tail_positions.add(self.tail_position)


@dataclass
class Position:
    x: int
    y: int

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))
