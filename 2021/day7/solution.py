import statistics

from base.solution import AdventOfCodeSolutionBase


class CrabSwarm:
    def __init__(self, starting_positions: list[int]):
        self.starting_positions = starting_positions

    def calculate_cheapest_alignment_cost(self) -> int:
        median_position = statistics.median(self.starting_positions)
        cost = 0
        for position in self.starting_positions:
            cost += abs(position - median_position)

        return int(cost)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: [int(v) for v in x.split(",") if x]

    def part1(self):
        crab_swarm = CrabSwarm(self.input_data[0])
        return crab_swarm.calculate_cheapest_alignment_cost()

    def part2(self):
        return None
