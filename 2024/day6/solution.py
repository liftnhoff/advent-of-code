from dataclasses import dataclass
from enum import Enum

import tqdm

from base.solution import AdventOfCodeSolutionBase


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


@dataclass
class GuardPosition:
    ri: int
    ci: int
    facing: Direction

    def __hash__(self):
        return hash((self.ri, self.ci, self.facing))

    def next_forward_position(self):
        if self.facing is Direction.UP:
            return GuardPosition(self.ri - 1, self.ci, self.facing)
        elif self.facing is Direction.DOWN:
            return GuardPosition(self.ri + 1, self.ci, self.facing)
        elif self.facing is Direction.LEFT:
            return GuardPosition(self.ri, self.ci - 1, self.facing)
        elif self.facing is Direction.RIGHT:
            return GuardPosition(self.ri, self.ci + 1, self.facing)

    def turn_right_position(self):
        if self.facing is Direction.UP:
            return GuardPosition(self.ri, self.ci, Direction.RIGHT)
        elif self.facing is Direction.DOWN:
            return GuardPosition(self.ri, self.ci, Direction.LEFT)
        elif self.facing is Direction.LEFT:
            return GuardPosition(self.ri, self.ci, Direction.UP)
        elif self.facing is Direction.RIGHT:
            return GuardPosition(self.ri, self.ci, Direction.DOWN)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        return len({(p.ri, p.ci) for p in self._get_all_guard_positions()})

    def _get_initial_guard_position(self):
        for ri, row in enumerate(self.input_data):
            for ci, value in enumerate(row):
                if value == "^":
                    return GuardPosition(ri, ci, Direction.UP)

    def _get_all_guard_positions(self):
        positions = [self._get_initial_guard_position()]
        while True:
            next_gp = positions[-1].next_forward_position()
            try:
                grid_value = self.input_data[next_gp.ri][next_gp.ci]
            except IndexError:
                break

            if grid_value == "#":
                positions.append(positions[-1].turn_right_position())
            else:
                positions.append(next_gp)

        return positions

    def part2(self):
        # loop_count = 0
        # pbar = tqdm.tqdm(
        #     desc="obstacle locations",
        #     total=len(self.input_data) * len(self.input_data[0]),
        # )
        # for ri, row in enumerate(self.input_data):
        #     for ci, value in enumerate(row):
        #         pbar.update(1)
        #         if value == "#" or value == "^":
        #             continue
        #
        #         if self._is_route_a_loop(ri, ci):
        #             loop_count += 1
        #
        # pbar.close()
        #
        # # 2260 is too high
        # return loop_count

        locations = {(p.ri, p.ci) for p in self._get_all_guard_positions()}
        loop_count = 0
        for ri, ci in tqdm.tqdm(locations, desc="obstacle locations"):
            value = self.input_data[ri][ci]
            if value != ".":
                continue
            if self._is_route_a_loop(ri, ci):
                loop_count += 1

        return loop_count

    def _is_route_a_loop(self, obstruction_ri, obstruction_ci) -> bool:
        positions = [self._get_initial_guard_position()]
        gp_set = {positions[-1]}
        is_loop = False
        while True:
            next_gp = positions[-1].next_forward_position()

            if next_gp in gp_set:
                is_loop = True
                break

            try:
                grid_value = self.input_data[next_gp.ri][next_gp.ci]
            except IndexError:
                break

            if grid_value == "#" or (
                next_gp.ri == obstruction_ri and next_gp.ci == obstruction_ci
            ):
                positions.append(positions[-1].turn_right_position())
            else:
                positions.append(next_gp)

            gp_set.add(positions[-1])

        return is_loop
