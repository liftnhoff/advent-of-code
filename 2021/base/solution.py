import abc
import os


class AdventOfCodeSolution(abc.ABC):
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_data = []

    def run(self):
        self.load_input_data()
        self.part1()
        self.part2()

    def load_input_data(self):
        input_file_path = os.path.join(self.input_file)
        with open(input_file_path) as fid:
            self.input_data = [line.rstrip() for line in fid]

    @abc.abstractmethod
    def part1(self):
        pass

    @abc.abstractmethod
    def part2(self):
        pass