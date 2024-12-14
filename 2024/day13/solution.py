import re

import numpy

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        token_count = 0
        epsilon = 1e-6

        button_a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
        button_b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
        prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
        x1, y1 = None, None
        x2, y2 = None, None
        xf, yf = None, None
        for line in self.input_data:
            if match := button_a_pattern.match(line):
                x1 = int(match.group(1))
                y1 = int(match.group(2))
            elif match := button_b_pattern.match(line):
                x2 = int(match.group(1))
                y2 = int(match.group(2))
            elif match := prize_pattern.match(line):
                xf = int(match.group(1))
                yf = int(match.group(2))
            else:
                coeffs = [
                    [x1, x2],
                    [y1, y2],
                ]
                consts = [xf, yf]
                ans = numpy.linalg.solve(coeffs, consts)
                if (
                    abs(ans[0] - numpy.round(ans[0])) < epsilon
                    and abs(ans[1] - numpy.round(ans[1])) < epsilon
                ):
                    token_count += int(3 * numpy.round(ans[0]) + numpy.round(ans[1]))

        return token_count

    def part2(self):
        token_count = 0
        epsilon = 1e-2

        button_a_pattern = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
        button_b_pattern = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
        prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")
        x1, y1 = None, None
        x2, y2 = None, None
        xf, yf = None, None
        for line in self.input_data:
            if match := button_a_pattern.match(line):
                x1 = int(match.group(1))
                y1 = int(match.group(2))
            elif match := button_b_pattern.match(line):
                x2 = int(match.group(1))
                y2 = int(match.group(2))
            elif match := prize_pattern.match(line):
                xf = int(match.group(1)) + 10000000000000
                yf = int(match.group(2)) + 10000000000000
            else:
                coeffs = [
                    [x1, x2],
                    [y1, y2],
                ]
                consts = [xf, yf]
                ans = numpy.linalg.solve(coeffs, consts)

                if (
                    abs(ans[0] - numpy.round(ans[0])) < epsilon
                    and abs(ans[1] - numpy.round(ans[1])) < epsilon
                ):
                    token_count += int(3 * numpy.round(ans[0]) + numpy.round(ans[1]))

        return token_count
