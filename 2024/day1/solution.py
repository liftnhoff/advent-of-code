from collections import Counter

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(y) for y in x.split("   "))

    def part1(self):
        left, right = list(zip(*self.input_data))
        dist = 0
        for a, b in zip(sorted(left), sorted(right)):
            dist += abs(b - a)

        return dist

    def part2(self):
        left, right = list(zip(*self.input_data))
        right_counts = Counter(right)
        score = 0
        for a in left:
            score += a * right_counts.get(a, 0)

        return score
