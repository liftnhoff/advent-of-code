import re

from base.solution import AdventOfCodeSolutionBase


class CommDevice:
    _NOOP_PATTERN = re.compile(r"^noop$")
    _ADDX_PATTERN = re.compile(r"^addx (-?\d+)$")

    def __init__(self):
        self.register = 1
        self.register_history = []

    def process_instruction(self, instruction: str) -> None:
        if self._NOOP_PATTERN.match(instruction):
            self.register_history.append(self.register)
        elif match := self._ADDX_PATTERN.match(instruction):
            self.register_history.append(self.register)
            self.register_history.append(self.register)

            value = int(match.group(1))
            self.register += value

    def signal_check_value(self) -> int:
        indices = [20, 60, 100, 140, 180, 220]
        check_value = 0
        for index in indices:
            check_value += index * self.register_history[index - 1]
        return check_value


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self) -> int:
        comm_device = CommDevice()
        for instruction in self.input_data:
            comm_device.process_instruction(instruction)
        return comm_device.signal_check_value()

    def part2(self):
        return None
