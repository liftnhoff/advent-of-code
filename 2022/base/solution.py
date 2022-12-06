import abc
import os
from typing import Any, Callable


class AdventOfCodeSolutionBase(abc.ABC):
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.input_data = tuple()

    def run(self):
        self._load_input_data()
        print(f"part 1: {self.part1()}")
        print(f"part 2: {self.part2()}")

    def _load_input_data(self):
        input_file_path = os.path.join(self.input_file)
        with open(input_file_path) as fid:
            self.input_data = tuple(self.data_parser()(line.rstrip()) for line in fid)

    @abc.abstractmethod
    def data_parser(self) -> Callable:
        """
        Returns a function that will operat on each line of data from the input file.
        """
        pass

    @abc.abstractmethod
    def part1(self) -> Any:
        """Calculate and return the answer to part 1."""
        pass

    @abc.abstractmethod
    def part2(self) -> Any:
        """Calculate and return the answer to part 2."""
        pass
