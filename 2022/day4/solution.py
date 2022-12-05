import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class SectionRange:
    start: int
    end: int


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(line: str) -> tuple[SectionRange, SectionRange]:
            pattern = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")
            if match := pattern.match(line):
                return (
                    SectionRange(int(match.group(1)), int(match.group(2))),
                    SectionRange(int(match.group(3)), int(match.group(4))),
                )

        return parser

    def part1(self):
        contained_pairs = 0
        for r1, r2 in self.input_data:
            if r1.start >= r2.start and r1.end <= r2.end:
                contained_pairs += 1
            elif r2.start >= r1.start and r2.end <= r1.end:
                contained_pairs += 1

        return contained_pairs

    def part2(self):
        return None
