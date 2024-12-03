import re

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        return robust_multiply_add("".join(self.input_data))

    def part2(self):
        cleaned = re.sub(r"don't\(\).*?do\(\)", "", "".join(self.input_data))
        return robust_multiply_add(cleaned)


def robust_multiply_add(instruction: str) -> int:
    output = 0
    regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    for match in regex.finditer(instruction):
        output += int(match.group(1)) * int(match.group(2))

    return output
