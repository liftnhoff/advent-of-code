from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        int_code = [int(x) for x in self.input_data[0].split(",")]
        int_code = process_int_code(int_code)
        return int_code

    def part2(self):
        return None


class Instruction:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    STOP = 99

    POSITION = 0
    IMMEDIATE = 1

    def __init__(self, instruction_code: int):
        self.op_code = instruction_code % 100
        self.p1_mode = instruction_code // 100 % 10
        self.p2_mode = instruction_code // 1000 % 10
        self.p3_mode = instruction_code // 10000 % 10

def process_int_code(int_code: list[int]) -> list[int]:
    output_buffer = []

    index = 0
    for _ in int_code:
        value = int_code[index]
        instruction = Instruction(value)
        if instruction.op_code == Instruction.ADD:
            p1 = int_code[index + 1]
            if instruction.p1_mode == Instruction.POSITION:
                p1 = int_code[p1]
            p2 = int_code[index + 2]
            if instruction.p2_mode == Instruction.POSITION:
                p2 = int_code[p2]

            p3 = int_code[index + 3]
            int_code[p3] = p1 + p2
            index += 4
        elif instruction.op_code == Instruction.MULTIPLY:
            p1 = int_code[index + 1]
            if instruction.p1_mode == Instruction.POSITION:
                p1 = int_code[p1]
            p2 = int_code[index + 2]
            if instruction.p2_mode == Instruction.POSITION:
                p2 = int_code[p2]

            p3 = int_code[index + 3]
            int_code[p3] = p1 * p2
            index += 4
        elif instruction.op_code == Instruction.INPUT:
            input_value = 1
            p1 = int_code[index + 1]
            int_code[p1] = input_value
            index += 2
        elif instruction.op_code == Instruction.OUTPUT:
            p1 = int_code[index + 1]
            output_buffer.append(p1)
            index += 2
        elif instruction.op_code == Instruction.STOP:
            break
    return output_buffer
