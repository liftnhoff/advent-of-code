import abc
import statistics

from base.solution import AdventOfCodeSolutionBase


class CrabSwarm(abc.ABC):
    def __init__(self, starting_positions: list[int]):
        self.starting_positions = starting_positions

    @abc.abstractmethod
    def calculate_cheapest_alignment_cost(self) -> int:
        pass


class ConstantCostCrabSwarm(CrabSwarm):
    def calculate_cheapest_alignment_cost(self) -> int:
        median_position = int(statistics.median(self.starting_positions))
        cost = 0
        for position in self.starting_positions:
            cost += abs(position - median_position)

        return cost


class LinearCostCrabSwarm(CrabSwarm):
    def calculate_cheapest_alignment_cost(self) -> int:
        # Guess the cheapest position at the median. Check the position to the right
        # and left to see if there is a cheaper position. Continue in that direction
        # until we find the minimum cost position.
        median_position = int(statistics.median(self.starting_positions))
        median_cost = self._calculate_cost_for_position(median_position)
        median_right_position = median_position + 1
        median_right_cost = self._calculate_cost_for_position(median_right_position)
        median_left_position = median_position - 1
        median_left_cost = self._calculate_cost_for_position(median_left_position)

        if median_right_cost < median_cost:
            cost = self._search_for_minimum_cost(
                median_right_position, median_right_cost, 1
            )
        elif median_left_cost < median_cost:
            cost = self._search_for_minimum_cost(
                median_left_position, median_left_cost, -1
            )
        else:
            cost = median_cost

        return cost

    def _calculate_cost_for_position(self, position: int) -> int:
        cost = 0
        for crab_position in self.starting_positions:
            distance = abs(position - crab_position)
            cost += sum_one_to_n(distance)

        return int(cost)

    def _search_for_minimum_cost(
        self, starting_position: int, starting_cost: int, direction_shift: int
    ) -> int:
        last_position = starting_position
        last_cost = starting_cost
        while True:
            position = last_position + direction_shift
            cost = self._calculate_cost_for_position(position)

            if cost > last_cost:
                cost = last_cost
                break
            else:
                last_position = position
                last_cost = cost

        return cost


def sum_one_to_n(n):
    return n * (n + 1) / 2


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: [int(v) for v in x.split(",") if x]

    def part1(self):
        crab_swarm = ConstantCostCrabSwarm(self.input_data[0])
        return crab_swarm.calculate_cheapest_alignment_cost()

    def part2(self):
        crab_swarm = LinearCostCrabSwarm(self.input_data[0])
        return crab_swarm.calculate_cheapest_alignment_cost()
