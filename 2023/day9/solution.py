from typing import Collection

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) for v in x.split())

    def part1(self):
        result = 0
        for sequence in self.input_data:
            result += self._extrapolate(sequence)
        return result

    def _extrapolate(self, sequence: tuple[int]) -> int:
        derivatives = self._get_all_derivatives(sequence)
        rate = 0
        for deltas in reversed(derivatives):
            rate += deltas[-1]

        return rate + sequence[-1]

    def _get_all_derivatives(self, sequence: Collection[int]) -> list[tuple[int]]:
        deltas = [tuple(bb - aa for aa, bb in zip(sequence, sequence[1:]))]

        if any(xx != 0 for xx in deltas[-1]):
            deltas.extend(self._get_all_derivatives(deltas[-1]))

        return deltas

    def _hindcast(self, sequence: tuple[int]) -> int:
        derivatives = self._get_all_derivatives(sequence)
        rate = 0
        for deltas in reversed(derivatives):
            rate = deltas[0] - rate

        return sequence[0] - rate

    def part2(self):
        result = 0
        for sequence in self.input_data:
            result += self._hindcast(sequence)
        return result
