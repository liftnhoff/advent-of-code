from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        min_range, max_range = (int(x) for x in self.input_data[0].split("-"))

        count = 0
        for value in range(min_range, max_range + 1):
            if meets_pw_criteria_p1(value):
                count += 1

        return count

    def part2(self):
        min_range, max_range = (int(x) for x in self.input_data[0].split("-"))

        count = 0
        for value in range(min_range, max_range + 1):
            if meets_pw_criteria_p2(value):
                count += 1

        return count


def meets_pw_criteria_p1(value: int) -> bool:
    str_value = str(value)
    has_double_digit = False
    has_increasing_digits = True
    for index in range(len(str_value) - 1):
        if str_value[index + 1] == str_value[index]:
            has_double_digit = True
        if int(str_value[index + 1]) < int(str_value[index]):
            has_increasing_digits = False

    return has_double_digit and has_increasing_digits


def meets_pw_criteria_p2(value: int) -> bool:
    str_value = str(value)
    has_double_digit = False
    has_increasing_digits = True
    last_digit = -1
    last_digit_count = 1
    for str_digit in str_value:
        current_digit = int(str_digit)
        if current_digit == last_digit:
            last_digit_count += 1
        else:
            if last_digit_count == 2:
                has_double_digit = True
            last_digit_count = 1

        if current_digit < last_digit:
            has_increasing_digits = False

        last_digit = current_digit

    if last_digit_count == 2:
        has_double_digit = True

    return has_double_digit and has_increasing_digits