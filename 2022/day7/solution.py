import re
from collections import defaultdict

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self) -> int:
        directory_sizes = self._get_directory_sizes()

        answer = 0
        for size in directory_sizes.values():
            if size <= 100_000:
                answer += size

        return answer

    def _get_directory_sizes(self) -> dict[str, int]:
        cd_pattern = re.compile(r"^\$ cd (\S+)$")
        file_pattern = re.compile(r"^(\d+) (\S+)$")

        current_directories = []
        directory_sizes = defaultdict(int)
        for line in self.input_data:
            if match := cd_pattern.match(line):
                directory = match.group(1)
                if directory == "..":
                    current_directories.pop()
                else:
                    current_directories.append(directory)
            elif match := file_pattern.match(line):
                size = int(match.group(1))
                for index in range(1, len(current_directories) + 1):
                    path = "/".join(current_directories[:index])
                    directory_sizes[path] += size

        return directory_sizes

    def part2(self) -> int:
        total_space = 70_000_000
        required_space = 30_000_000

        directory_sizes = self._get_directory_sizes()
        used_space = directory_sizes["/"]
        unused_space = total_space - used_space
        minimum_size = required_space - unused_space
        for size in sorted(directory_sizes.values()):
            if size >= minimum_size:
                return size
