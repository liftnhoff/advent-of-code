from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return int

    def part1(self):
        step_increase_count = 0
        for index in range(1, len(self.input_data)):
            if self.input_data[index] > self.input_data[index - 1]:
                step_increase_count += 1

        print(f"part 1: {step_increase_count}")

    def part2(self):
        window_increase_count = 0
        for index in range(1, len(self.input_data) - 1):
            current_window_sum = sum(self.input_data[index - 1 : index + 2])
            next_window_sum = sum(self.input_data[index : index + 3])
            if next_window_sum > current_window_sum:
                window_increase_count += 1

        print(f"part 2: {window_increase_count}")
