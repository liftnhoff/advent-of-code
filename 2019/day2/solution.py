from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        int_code = [int(x) for x in self.input_data[0].split(",")]
        int_code[1] = 12
        int_code[2] = 2
        int_code = process_int_code(int_code)
        return int_code[0]

    def part2(self):
        input_code = tuple(int(x) for x in self.input_data[0].split(","))
        for noun in range(100):
            for verb in range(100):
                int_code = list(input_code)
                int_code[1] = noun
                int_code[2] = verb
                int_code = process_int_code(int_code)
                if int_code[0] == 19690720:
                    return 100 * noun + verb


def process_int_code(int_code: list[int]) -> list[int]:
    add = 1
    multiply = 2
    stop = 99

    index = 0
    for _ in int_code:
        value = int_code[index]
        if value == add:
            p1 = int_code[index + 1]
            p2 = int_code[index + 2]
            p3 = int_code[index + 3]
            int_code[p3] = int_code[p1] + int_code[p2]
            index += 4
        elif value == multiply:
            p1 = int_code[index + 1]
            p2 = int_code[index + 2]
            p3 = int_code[index + 3]
            int_code[p3] = int_code[p1] * int_code[p2]
            index += 4
        elif value == stop:
            break
    return int_code
