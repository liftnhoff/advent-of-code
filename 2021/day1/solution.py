from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def part1(self):
        step_increase_count = 0
        current = int(self.input_data[0])
        for index in range(1, len(self.input_data)):
            next = int(self.input_data[index])
            if next > current:
                step_increase_count += 1
            current = next

        print(f"part 1: {step_increase_count}")

    def part2(self):
        pass
