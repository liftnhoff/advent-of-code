from typing import Union, List, Tuple

from base.solution import AdventOfCodeSolutionBase


class BingoBoard:
    _WINNING_INDEX_SETS = (
        frozenset({0, 1, 2, 3, 4}),  # rows
        frozenset({5, 6, 7, 8, 9}),
        frozenset({10, 11, 12, 13, 14}),
        frozenset({15, 16, 17, 18, 19}),
        frozenset({20, 21, 22, 23, 24}),
        frozenset({0, 5, 10, 15, 20}),  # columns
        frozenset({1, 6, 11, 16, 21}),
        frozenset({2, 7, 12, 17, 22}),
        frozenset({3, 8, 13, 18, 23}),
        frozenset({4, 9, 14, 19, 24}),
    )

    def __init__(self, board_values: Union[List[int], Tuple[int]]):
        if len(board_values) != 25:
            raise ValueError("A BingoBoard requires 25 values.")
        self.board_values = tuple(board_values)
        self.seen_indexes = set()

    def __repr__(self):
        return f"BingoBoard ({''.join(str(x) for x in self.board_values)})"

    def __str__(self):
        output_rows = [
            self.__repr__(),
            "".join(f"{x: 4d}" for x in self.board_values[0:5]),
            "".join(f"{x: 4d}" for x in self.board_values[5:10]),
            "".join(f"{x: 4d}" for x in self.board_values[10:15]),
            "".join(f"{x: 4d}" for x in self.board_values[15:20]),
            "".join(f"{x: 4d}" for x in self.board_values[20:25]),
        ]
        return "\n".join(output_rows)

    def maybe_add_number_and_check_bingo(self, number: int) -> bool:
        """
        See if a number is on the board and if it is see if this board won.

        Returns True if the board wins with the provided number, False if not.
        """
        for index, board_value in enumerate(self.board_values):
            if number == board_value:
                self.seen_indexes.add(index)

                for winning_set in self._WINNING_INDEX_SETS:
                    if winning_set.issubset(self.seen_indexes):
                        return True

        return False

    def get_unmarked_numbers(self) -> List[int]:
        unmarked_numbers = []
        for index, number in enumerate(self.board_values):
            if index not in self.seen_indexes:
                unmarked_numbers.append(number)

        return unmarked_numbers


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        numbers, bingo_boards = self._prepare_bingo()
        for number in numbers:
            for board in bingo_boards:
                if board.maybe_add_number_and_check_bingo(number):
                    return number * sum(board.get_unmarked_numbers())

        return "No winning board was found."

    def _prepare_bingo(self) -> Tuple[Tuple[int], List[BingoBoard]]:
        numbers = tuple(int(x) for x in self.input_data[0].split(","))

        bingo_boards = []
        board_values = []
        for line in self.input_data[2:]:
            if line == "":
                bingo_boards.append(BingoBoard(board_values))
                board_values = []

            board_values.extend(int(x) for x in line.split())

        if board_values:
            bingo_boards.append(BingoBoard(board_values))

        return numbers, bingo_boards

    def part2(self):
        numbers, bingo_boards = self._prepare_bingo()

        last_winning_number = None
        last_winning_board = None
        for number in numbers:
            losing_bingo_boards = []

            for board in bingo_boards:
                if board.maybe_add_number_and_check_bingo(number):
                    last_winning_number = number
                    last_winning_board = board
                else:
                    losing_bingo_boards.append(board)

            bingo_boards = losing_bingo_boards

        return last_winning_number * sum(last_winning_board.get_unmarked_numbers())
