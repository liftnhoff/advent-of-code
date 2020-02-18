import argparse
from typing import List


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true')
    args = parser.parse_args()

    if args.test:
        test_sample_input()
        return

    # part 1
    data = read_data()
    data[1] = 12
    data[2] = 2
    computer = IntcodeComputer()
    results = computer.process_intcode(data)
    print(results)

    part2()


def test_sample_input():
    computer = IntcodeComputer()
    assert computer.process_intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert computer.process_intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert computer.process_intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert computer.process_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    print('Sample input tests pass.')


def read_data() -> List[int]:
    with open('data.txt') as fid:
        data = [int(x) for x in fid.readline().split(',')]
    return data


class IntcodeComputer:
    _ADD = 1
    _MULTIPLY = 2
    _STEP_SIZE = 4
    _STOP = 99

    def process_intcode(self, intcode: List[int]) -> List[int]:
        index = 0
        while True:
            opcode = intcode[index]
            if opcode == self._ADD:
                value1_index = intcode[index + 1]
                value2_index = intcode[index + 2]
                position = intcode[index + 3]
                intcode[position] = intcode[value1_index] + intcode[value2_index]
                index += self._STEP_SIZE
            elif opcode == self._MULTIPLY:
                value1_index = intcode[index + 1]
                value2_index = intcode[index + 2]
                position = intcode[index + 3]
                intcode[position] = intcode[value1_index] * intcode[value2_index]
                index += self._STEP_SIZE
            elif opcode == self._STOP:
                break
            else:
                print('ERROR: Unknown opcode.')
                break

        return intcode


def part2():
    answer = 19690720
    computer = IntcodeComputer()
    for noun in range(0, 100):
        for verb in range(0, 100):
            data = read_data()
            data[1] = noun
            data[2] = verb
            results = computer.process_intcode(data)
            if results[0] == answer:
                print(f'Part 2 answer: {100 * noun + verb}')
                return


if __name__ == '__main__':
    main()
