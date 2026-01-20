from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: int(x)

    def part1(self):
        total = 0
        for mass in self.input_data:
            total += mass // 3 - 2
        return total

    def part2(self):
        total = 0
        for mass in self.input_data:
            mass = mass // 3 - 2
            while mass > 0:
                total += mass
                mass = mass // 3 - 2
        return total
