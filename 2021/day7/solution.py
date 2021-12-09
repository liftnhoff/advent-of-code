import abc
import statistics

from base.solution import AdventOfCodeSolutionBase


class CrabSwarm(abc.ABC):
    def __init__(self, starting_positions: list[int]):
        self.starting_positions = starting_positions

    @abc.abstractmethod
    def calculate_cheapest_alignment_cost(self) -> int:
        pass


class ConstantCrabSwarm(CrabSwarm):
    def calculate_cheapest_alignment_cost(self) -> int:
        median_position = int(statistics.median(self.starting_positions))
        cost = 0
        for position in self.starting_positions:
            cost += abs(position - median_position)

        return cost


class LinearCrabSwarm(CrabSwarm):
    def calculate_cheapest_alignment_cost(self) -> int:
        median_position = int(statistics.median(self.starting_positions))
        median_cost = self._calculate_cost_for_position(median_position)
        median_right_position = median_position + 1
        median_right_cost = self._calculate_cost_for_position(median_right_position)
        median_left_position = median_position - 1
        median_left_cost = self._calculate_cost_for_position(median_left_position)

        if median_right_cost < median_cost:
            last_position = median_right_position
            last_cost = median_right_cost
            while True:
                position = last_position + 1
                cost = self._calculate_cost_for_position(position)

                if cost > last_cost:
                    cost = last_cost
                    break
                else:
                    last_position = position
                    last_cost = cost

        elif median_left_cost < median_cost:
            last_position = median_left_position
            last_cost = median_left_cost
            while True:
                position = last_position - 1
                cost = self._calculate_cost_for_position(position)

                if cost > last_cost:
                    cost = last_cost
                    break
                else:
                    last_position = position
                    last_cost = cost

        else:
            cost = median_cost

        return cost

    def _calculate_cost_for_position(self, position: int) -> int:
        cost = 0
        for crab_position in self.starting_positions:
            distance = abs(position - crab_position)
            # Use the n*(n+1)/2 formula for the sum of 1 to n.
            cost += distance * (distance + 1) / 2

        return int(cost)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: [int(v) for v in x.split(",") if x]

    def part1(self):
        crab_swarm = ConstantCrabSwarm(self.input_data[0])
        return crab_swarm.calculate_cheapest_alignment_cost()

    def part2(self):
        crab_swarm = LinearCrabSwarm(self.input_data[0])
        return crab_swarm.calculate_cheapest_alignment_cost()
