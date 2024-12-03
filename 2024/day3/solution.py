import re

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        output = 0
        regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
        for match in regex.finditer("".join(self.input_data)):
            output += int(match.group(1)) * int(match.group(2))

        return output

    def part2(self):
        cleaned = re.sub(r"don't\(\).*?do\(\)", "", "".join(self.input_data))

        output = 0
        regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
        for match in regex.finditer(cleaned):
            output += int(match.group(1)) * int(match.group(2))

        return output
