from collections import deque

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: tuple(int(v) for v in x.split())

    def part1(self):
        safe_count = 0
        for report in self.input_data:
            if is_report_safe(report):
                safe_count += 1

        return safe_count

    def part2(self):
        safe_count = 0
        for report in self.input_data:
            if is_report_safe(report):
                safe_count += 1
            else:
                results = []
                for index in range(len(report)):
                    levels = list(report)
                    levels.pop(index)
                    results.append(is_report_safe(levels))

                if any(results):
                    safe_count += 1

        return safe_count


def is_report_safe(report) -> bool:
    is_safe = True
    is_decreasing = report[1] < report[0]

    for index in range(1, len(report)):
        delta = abs(report[index] - report[index - 1])
        if not 1 <= delta <= 3:
            is_safe = False
            break

        if is_decreasing and report[index] > report[index - 1]:
            is_safe = False
            break

        if not is_decreasing and report[index] < report[index - 1]:
            is_safe = False
            break

    return is_safe
