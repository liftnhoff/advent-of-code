from enum import IntEnum

from base.solution import AdventOfCodeSolutionBase


class GamePoints(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


class Play(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def parser(x: str) -> tuple[Play, Play]:
            you, me = x.split(" ")
            if you == "A":
                your_play = Play.ROCK
            elif you == "B":
                your_play = Play.PAPER
            elif you == "C":
                your_play = Play.SCISSORS
            else:
                raise RuntimeError(f"Invalid input for your play '{you}'")

            if me == "X":
                my_play = Play.ROCK
            elif me == "Y":
                my_play = Play.PAPER
            elif me == "Z":
                my_play = Play.SCISSORS
            else:
                raise RuntimeError(f"Invalid input for my play '{me}'")

            return your_play, my_play

        return parser

    def part1(self) -> int:
        my_score_matrix = {
            (Play.ROCK, Play.ROCK): Play.ROCK + GamePoints.DRAW,
            (Play.ROCK, Play.PAPER): Play.PAPER + GamePoints.WIN,
            (Play.ROCK, Play.SCISSORS): Play.SCISSORS + GamePoints.LOSS,
            (Play.PAPER, Play.ROCK): Play.ROCK + GamePoints.LOSS,
            (Play.PAPER, Play.PAPER): Play.PAPER + GamePoints.DRAW,
            (Play.PAPER, Play.SCISSORS): Play.SCISSORS + GamePoints.WIN,
            (Play.SCISSORS, Play.ROCK): Play.ROCK + GamePoints.WIN,
            (Play.SCISSORS, Play.PAPER): Play.PAPER + GamePoints.LOSS,
            (Play.SCISSORS, Play.SCISSORS): Play.SCISSORS + GamePoints.DRAW,
        }

        my_total_score = 0
        for your_play, my_play in self.input_data:
            my_total_score += my_score_matrix[(your_play, my_play)]

        return my_total_score

    def part2(self):
        return None
