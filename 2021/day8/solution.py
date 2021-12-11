from collections import defaultdict
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class DisplayInfo:
    input_signals: list[set[str]]
    output_values: list[set[str]]


class SegmentMapper:
    """
     aaaa
    b    c
    b    c
     dddd
    e    f
    e    f
     gggg
    """

    NUMBERS_BY_SEGMENT_GROUP = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    def __init__(self, input_signals: list[str]):
        self.input_signals = input_signals

        self.canonical_by_current: dict[str, str] = {}
        self.current_by_canonical: dict[str, str] = {}
        self.segment_group_by_number: dict[int, set[str]] = {}
        self.segment_groups_by_length: dict[int, set[str]] = defaultdict(list)

    def identify_number(self, segment_group: set[str]) -> int:
        self._map_to_standard_segments_if_needed()

        mapped_set = set()
        for segment in segment_group:
            mapped_set.add(self.canonical_by_current[segment])

        return self.NUMBERS_BY_SEGMENT_GROUP["".join(sorted(mapped_set))]

    def _map_to_standard_segments_if_needed(self):
        if self.canonical_by_current:
            return

        self._initialize_known_values()
        self._get_mapping_for_a()
        self._get_segment_for_9()
        self._get_mapping_for_g()
        self._get_segment_for_3()
        self._get_mapping_for_b()
        self._get_mapping_for_d()
        self._get_segment_for_5()
        self._get_mapping_for_f()
        self._get_mapping_for_c()
        self._get_segment_for_2()
        self._get_mapping_for_e()

    def _initialize_known_values(self):
        for segments in self.input_signals:
            self.segment_groups_by_length[len(segments)].append(segments)

        self.segment_group_by_number[1] = self.segment_groups_by_length[2][0]
        self.segment_group_by_number[4] = self.segment_groups_by_length[4][0]
        self.segment_group_by_number[7] = self.segment_groups_by_length[3][0]
        self.segment_group_by_number[8] = self.segment_groups_by_length[7][0]

    def _get_mapping_for_a(self):
        key = (
            self.segment_group_by_number[7]
            .difference(self.segment_group_by_number[1])
            .pop()
        )

        self.canonical_by_current[key] = "a"
        self.current_by_canonical["a"] = key

    def _get_segment_for_9(self):
        for segment_group in self.segment_groups_by_length[6]:
            if self.segment_group_by_number[4].issubset(segment_group):
                self.segment_group_by_number[9] = segment_group
                break

    def _get_mapping_for_g(self):
        key = (
            self.segment_group_by_number[9]
            .difference(self.segment_group_by_number[4])
            .difference(self.current_by_canonical["a"])
        ).pop()

        self.canonical_by_current[key] = "g"
        self.current_by_canonical["g"] = key

    def _get_segment_for_3(self):
        for segment_group in self.segment_groups_by_length[5]:
            if self.segment_group_by_number[1].issubset(segment_group):
                self.segment_group_by_number[3] = segment_group
                break

    def _get_mapping_for_b(self):
        key = (
            self.segment_group_by_number[9]
            .difference(self.segment_group_by_number[3])
            .pop()
        )

        self.canonical_by_current[key] = "b"
        self.current_by_canonical["b"] = key

    def _get_mapping_for_d(self):
        key = (
            self.segment_group_by_number[4]
            .difference(self.segment_group_by_number[1])
            .difference(self.current_by_canonical["b"])
        ).pop()

        self.canonical_by_current[key] = "d"
        self.current_by_canonical["d"] = key

    def _get_segment_for_5(self):
        for segment_group in self.segment_groups_by_length[5]:
            if self.current_by_canonical["b"] in segment_group:
                self.segment_group_by_number[5] = segment_group
                break

    def _get_mapping_for_f(self):
        key = (
            self.segment_group_by_number[5]
            .difference(
                {
                    self.current_by_canonical["a"],
                    self.current_by_canonical["b"],
                    self.current_by_canonical["d"],
                    self.current_by_canonical["g"],
                }
            )
            .pop()
        )

        self.canonical_by_current[key] = "f"
        self.current_by_canonical["f"] = key

    def _get_mapping_for_c(self):
        key = (
            self.segment_group_by_number[1]
            .difference(self.current_by_canonical["f"])
            .pop()
        )

        self.canonical_by_current[key] = "c"
        self.current_by_canonical["c"] = key

    def _get_segment_for_2(self):
        for segment_group in self.segment_groups_by_length[5]:
            if (
                segment_group != self.segment_group_by_number[3]
                and segment_group != self.segment_group_by_number[5]
            ):
                self.segment_group_by_number[2] = segment_group
                break

    def _get_mapping_for_e(self):
        key = (
            self.segment_group_by_number[2]
            .difference(
                {
                    self.current_by_canonical["a"],
                    self.current_by_canonical["c"],
                    self.current_by_canonical["d"],
                    self.current_by_canonical["g"],
                }
            )
            .pop()
        )

        self.canonical_by_current[key] = "e"
        self.current_by_canonical["e"] = key


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(line):
            input_signals, output_values = line.split("|")
            return DisplayInfo(
                [set(segments) for segments in input_signals.split()],
                [set(segments) for segments in output_values.split()],
            )

        return parser

    def part1(self):
        unique_segment_counts_set = {2, 3, 4, 7}

        unique_counts_total = 0
        for display_info in self.input_data:
            for output_value in display_info.output_values:
                if len(output_value) in unique_segment_counts_set:
                    unique_counts_total += 1

        return unique_counts_total

    def part2(self):
        total = 0
        for display_info in self.input_data:
            mapper = SegmentMapper(display_info.input_signals)
            digits = []
            for output_value in display_info.output_values:
                digits.append(mapper.identify_number(output_value))

            total += digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[1]

        return total
