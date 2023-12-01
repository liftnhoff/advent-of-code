import re

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        # Note that the test input is different between days, this won't work with the
        # current test input.
        numbers = []
        for row in self.input_data:
            row_numbers = []
            for value in row:
                try:
                    number = int(value)
                except ValueError:
                    continue
                row_numbers.append(number)
            numbers.append(int(f"{row_numbers[0]}{row_numbers[-1]}"))

        return sum(numbers)

    def part2(self):
        # build the ridiculous smashed number strings like "eighthree"
        number_lookup = {}
        numbers = (
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        )
        for xi, xx in enumerate(numbers, start=1):
            for yi, yy in enumerate(numbers, start=1):
                smashed_number = xx + yy[1:]
                number_lookup[smashed_number] = f"{xi}{yi}"

        number_lookup.update(
            {
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
            }
        )

        regex = re.compile(f"({'|'.join(number_lookup.keys())})")
        numbers = []
        for row in self.input_data:
            row_numbers = regex.findall(row)
            parsed_numbers = []
            for value in row_numbers:
                number = number_lookup[value]
                if len(number) > 1:
                    parsed_numbers.extend(number)
                else:
                    parsed_numbers.append(number)

            numbers.append(int(parsed_numbers[0] + parsed_numbers[-1]))

        return sum(numbers)
