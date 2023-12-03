from collections import deque

from base.solution import AdventOfCodeSolutionBase

# sed -E 's/(.)/\1\n/g' input.txt | sort -u | grep -v -P '\d|\.'
SYMBOLS = frozenset(("#", "$", "%", "&", "*", "+", "-", "/", "=", "@"))
NUMBERS = frozenset(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        numbers = []
        for row_index, row in enumerate(self.input_data):
            for col_index, value in enumerate(row):
                if value in SYMBOLS:
                    numbers.extend(self._get_nearby_numbers(row_index, col_index))

        return sum(numbers)

    def _get_nearby_numbers(self, row_index: int, col_index: int) -> set[int]:
        numbers = set()
        for ri in range(row_index - 1, row_index + 2):
            if ri < 0 or ri >= len(self.input_data):
                continue
            for ci in range(col_index - 1, col_index + 2):
                if ci < 0 or ci >= len(self.input_data[0]):
                    continue

                value = self.input_data[ri][ci]
                if value in NUMBERS:
                    numbers.add(self._scan_full_number(ri, ci))

        return numbers

    def _scan_full_number(self, row_index: int, col_index: int) -> int:
        number_deque = deque()
        ci = col_index
        while ci >= 0:
            value = self.input_data[row_index][ci]
            if value in NUMBERS:
                number_deque.appendleft(value)
                ci -= 1
            else:
                break

        ci = col_index + 1
        while ci < len(self.input_data[row_index]):
            value = self.input_data[row_index][ci]
            if value in NUMBERS:
                number_deque.append(value)
                ci += 1
            else:
                break

        return int("".join(number_deque))

    def part2(self):
        gear_ratios = []
        gear_symbol = "*"
        for row_index, row in enumerate(self.input_data):
            for col_index, value in enumerate(row):
                if value == gear_symbol:
                    gear_ratios.append(self._get_gear_ratio(row_index, col_index))

        return sum(gear_ratios)

    def _get_gear_ratio(self, row_index: int, col_index: int) -> int:
        numbers = set()
        for ri in range(row_index - 1, row_index + 2):
            if ri < 0 or ri >= len(self.input_data):
                continue
            for ci in range(col_index - 1, col_index + 2):
                if ci < 0 or ci >= len(self.input_data[0]):
                    continue

                value = self.input_data[ri][ci]
                if value in NUMBERS:
                    numbers.add(self._scan_full_number(ri, ci))

        if len(numbers) == 2:
            gear1, gear2 = list(numbers)
            gear_ratio = gear1 * gear2
        else:
            gear_ratio = 0

        return gear_ratio
