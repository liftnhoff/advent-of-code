import itertools

import tqdm

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
        return self._check_operators(operators)

    def _check_operators(self, operators):
        total = 0
        for ans, inputs in tqdm.tqdm(self.input_data):
            operator_permutations = list(
                itertools.product(operators, repeat=len(inputs) - 1)
            )

            for ops in operator_permutations:
                current = inputs[0]
                for index, op in enumerate(ops):
                    current = op(current, inputs[index + 1])

                if current == ans:
                    total += current
                    break

        return total

    def part2(self):
        operators = (add, mul, cat)
        return self._check_operators(operators)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def cat(a, b):
    return int(f"{a}{b}")
