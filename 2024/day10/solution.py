from collections import deque, OrderedDict, defaultdict
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Position:
    ri: int
    ci: int

    def __hash__(self):
        return hash((self.ri, self.ci))

    def up(self):
        return Position(self.ri - 1, self.ci)

    def down(self):
        return Position(self.ri + 1, self.ci)

    def left(self):
        return Position(self.ri, self.ci - 1)

    def right(self):
        return Position(self.ri, self.ci + 1)


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) if v != "." else v for v in x)

    def part1(self):
        paths = deque()
        for ri, row in enumerate(self.input_data):
            for ci, value in enumerate(row):
                if value == 0:
                    paths.append(OrderedDict({Position(ri, ci): value}))

        peaks_by_trailhead = defaultdict(set)
        while paths:
            path = paths.popleft()
            pos, value = list(path.items())[-1]
            if value == 9:
                steps = list(path.keys())
                peaks_by_trailhead[steps[0]].add(steps[-1])
            else:
                possible_steps = self._possible_steps(path, pos, value)
                if len(possible_steps) == 1:
                    step = possible_steps[0]
                    path[step] = self.input_data[step.ri][step.ci]
                    paths.appendleft(path)
                else:
                    for step in possible_steps:
                        new_path = OrderedDict(path)
                        new_path[step] = self.input_data[step.ri][step.ci]
                        paths.appendleft(new_path)

        score = 0
        for peaks in peaks_by_trailhead.values():
            score += len(peaks)

        return score

    def _possible_steps(self, path, pos, value):
        possible_steps = []
        up = pos.up()
        if self._is_in_bounds(up) and up not in path:
            up_value = self.input_data[up.ri][up.ci]
            if up_value - value == 1:
                possible_steps.append(up)

        down = pos.down()
        if self._is_in_bounds(down) and down not in path:
            down_value = self.input_data[down.ri][down.ci]
            if down_value - value == 1:
                possible_steps.append(down)

        left = pos.left()
        if self._is_in_bounds(left) and left not in path:
            left_value = self.input_data[left.ri][left.ci]
            if left_value - value == 1:
                possible_steps.append(left)

        right = pos.right()
        if self._is_in_bounds(right) and right not in path:
            right_value = self.input_data[right.ri][right.ci]
            if right_value - value == 1:
                possible_steps.append(right)

        return possible_steps

    def _is_in_bounds(self, pos):
        return 0 <= pos.ri < len(self.input_data) and 0 <= pos.ci < len(
            self.input_data[0]
        )

    def part2(self):
        paths = deque()
        for ri, row in enumerate(self.input_data):
            for ci, value in enumerate(row):
                if value == 0:
                    paths.append(OrderedDict({Position(ri, ci): value}))

        score = 0
        while paths:
            path = paths.popleft()
            pos, value = list(path.items())[-1]
            if value == 9:
                score += 1
            else:
                possible_steps = self._possible_steps(path, pos, value)
                if len(possible_steps) == 1:
                    step = possible_steps[0]
                    path[step] = self.input_data[step.ri][step.ci]
                    paths.appendleft(path)
                else:
                    for step in possible_steps:
                        new_path = OrderedDict(path)
                        new_path[step] = self.input_data[step.ri][step.ci]
                        paths.appendleft(new_path)

        return score
