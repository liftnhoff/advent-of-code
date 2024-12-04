import re
from collections import defaultdict

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        count = 0
        grid_slices = get_all_grid_slices(self.input_data)
        pattern = re.compile(r"XMAS")
        for grid_slice in grid_slices:
            count += len(pattern.findall("".join(grid_slice)))

        return count

    def part2(self):
        count = 0
        for ri, row in enumerate(self.input_data):
            if ri == 0 or ri == len(self.input_data) - 1:
                continue

            for ci, value in enumerate(row):
                if ci == 0 or ci == len(row) - 1:
                    continue

                if value == "A":
                    if (
                        self.input_data[ri - 1][ci - 1] == "M"
                        and self.input_data[ri + 1][ci + 1] == "S"
                        and self.input_data[ri - 1][ci + 1] == "M"
                        and self.input_data[ri + 1][ci - 1] == "S"
                    ):
                        count += 1
                    elif (
                        self.input_data[ri - 1][ci - 1] == "S"
                        and self.input_data[ri + 1][ci + 1] == "M"
                        and self.input_data[ri - 1][ci + 1] == "M"
                        and self.input_data[ri + 1][ci - 1] == "S"
                    ):
                        count += 1
                    elif (
                        self.input_data[ri - 1][ci - 1] == "M"
                        and self.input_data[ri + 1][ci + 1] == "S"
                        and self.input_data[ri - 1][ci + 1] == "S"
                        and self.input_data[ri + 1][ci - 1] == "M"
                    ):
                        count += 1
                    elif (
                        self.input_data[ri - 1][ci - 1] == "S"
                        and self.input_data[ri + 1][ci + 1] == "M"
                        and self.input_data[ri - 1][ci + 1] == "S"
                        and self.input_data[ri + 1][ci - 1] == "M"
                    ):
                        count += 1

        return count


def get_all_grid_slices(list_of_lists):
    # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
    # with a tweak from me to get the reverse of all slices as well.

    grid_slices = []
    cols = _grid_slice(list_of_lists, lambda x, y: x)
    grid_slices.extend(cols)
    grid_slices.extend(reversed(v) for v in cols)
    rows = _grid_slice(list_of_lists, lambda x, y: y)
    grid_slices.extend(rows)
    grid_slices.extend(reversed(v) for v in rows)
    fdiag = _grid_slice(list_of_lists, lambda x, y: x + y)
    grid_slices.extend(fdiag)
    grid_slices.extend(reversed(v) for v in fdiag)
    bdiag = _grid_slice(list_of_lists, lambda x, y: x - y)
    grid_slices.extend(bdiag)
    grid_slices.extend(reversed(v) for v in bdiag)

    return grid_slices


def _grid_slice(data, func):
    slices = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            slices[func(x, y)].append(data[y][x])
    return list(map(slices.get, sorted(slices.keys())))
