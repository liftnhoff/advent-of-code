from typing import Union

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
        frozenset({0, 6, 12, 18, 24}),  # diagonals
        frozenset({4, 8, 12, 16, 20}),
    )

    def __init__(self, board_values: Union[list[int], tuple[int]]):
        if len(board_values) != 25:
            raise ValueError("A BingoBoard requires 25 values.")
        self.board_values = tuple(board_values)
        self.seen_indexes = set()

    def __repr__(self):
        output_rows = [
            "BingoBoard",
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


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        numbers, bingo_boards = self._prepare_bingo()
        print(numbers)
        for b in bingo_boards:
            print(b)
        return None

    def _prepare_bingo(self) -> tuple[tuple[int], list[BingoBoard]]:
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
        return None
