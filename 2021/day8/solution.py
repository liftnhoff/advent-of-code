from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class DisplayInfo:
    input_signals: list[str]
    output_values: list[str]

    NUMBERS_BY_SEGMENT_COUNTS = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8],
    }


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(line):
            input_signals, output_values = line.split("|")
            return DisplayInfo(input_signals.split(), output_values.split())

        return parser

    def part1(self):
        unique_segment_counts_set = {
            key
            for key, value in DisplayInfo.NUMBERS_BY_SEGMENT_COUNTS.items()
            if len(value) == 1
        }

        unique_counts_total = 0
        for display_info in self.input_data:
            for output_value in display_info.output_values:
                if len(output_value) in unique_segment_counts_set:
                    unique_counts_total += 1

        return unique_counts_total

    def part2(self):
        return None
