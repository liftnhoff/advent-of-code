from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: int(x) if x else None

    def part1(self):
        calorie_counts = []
        current_pack = []
        for calories in self.input_data:
            if calories is None:
                calorie_counts.append(sum(current_pack))
                current_pack = []
            else:
                current_pack.append(calories)

        calorie_counts.append(sum(current_pack))

        return max(calorie_counts)

    def part2(self):
        return None
