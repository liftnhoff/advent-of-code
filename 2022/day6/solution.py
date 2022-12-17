from collections import deque

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self) -> int:
        marker_width = 4
        start_index = marker_width - 1

        index = -1
        for code in self.input_data:
            current_chars = deque(code[:start_index])
            for index, value in enumerate(code[start_index:], start=marker_width):
                current_chars.append(value)
                if len(set(current_chars)) == len(current_chars):
                    print(index)
                    break
                current_chars.popleft()

        return index

    def part2(self):
        marker_width = 14
        start_index = marker_width - 1

        index = -1
        for code in self.input_data:
            current_chars = deque(code[:start_index])
            for index, value in enumerate(code[start_index:], start=marker_width):
                current_chars.append(value)
                if len(set(current_chars)) == len(current_chars):
                    print(index)
                    break
                current_chars.popleft()

        return index
