import itertools

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def line_parser(line: str):
            ans, inputs = line.split(":")
            ans = int(ans)
            inputs = tuple(int(v.strip()) for v in inputs.split())
            return ans, inputs

        return line_parser

    def part1(self):
        operators = (add, mul)
        for ans, inputs in self.input_data:
            operator_permutations = list(
                itertools.product(operators, repeat=len(inputs) - 1)
            )

            # for ops in operator_permutations:
            #     current = 0
            #     for index, op in enumerate(ops):

        return None

    def part2(self):
        return None


def add(a, b):
    return a + b


def mul(a, b):
    return a * b
