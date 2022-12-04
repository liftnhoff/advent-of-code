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
        return lambda x: x

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
        for line in self.input_data:
            your_play, my_play = self._opponent_and_me_interpretation(line)
            my_total_score += my_score_matrix[(your_play, my_play)]

        return my_total_score

    def _opponent_and_me_interpretation(self, line: str):
        you, me = line.split(" ")
        if you == "A":
            your_play = Play.ROCK
        elif you == "B":
            your_play = Play.PAPER
        elif you == "C":
            your_play = Play.SCISSORS
        else:
            raise RuntimeError(f"Invalid input for opponent play '{you}'")

        if me == "X":
            my_play = Play.ROCK
        elif me == "Y":
            my_play = Play.PAPER
        elif me == "Z":
            my_play = Play.SCISSORS
        else:
            raise RuntimeError(f"Invalid input for my play '{me}'")

        return your_play, my_play

    def part2(self) -> int:
        my_score_matrix = {
            (Play.ROCK, GamePoints.LOSS): GamePoints.LOSS + Play.SCISSORS,
            (Play.ROCK, GamePoints.DRAW): GamePoints.DRAW + Play.ROCK,
            (Play.ROCK, GamePoints.WIN): GamePoints.WIN + Play.PAPER,
            (Play.PAPER, GamePoints.LOSS): GamePoints.LOSS + Play.ROCK,
            (Play.PAPER, GamePoints.DRAW): GamePoints.DRAW + Play.PAPER,
            (Play.PAPER, GamePoints.WIN): GamePoints.WIN + Play.SCISSORS,
            (Play.SCISSORS, GamePoints.LOSS): GamePoints.LOSS + Play.PAPER,
            (Play.SCISSORS, GamePoints.DRAW): GamePoints.DRAW + Play.SCISSORS,
            (Play.SCISSORS, GamePoints.WIN): GamePoints.WIN + Play.ROCK,
        }

        my_total_score = 0
        for line in self.input_data:
            your_play, outcome = self._opponent_and_outcome_interpretation(line)
            my_total_score += my_score_matrix[(your_play, outcome)]

        return my_total_score

    def _opponent_and_outcome_interpretation(self, line: str):
        you, outcome_code = line.split(" ")
        if you == "A":
            your_play = Play.ROCK
        elif you == "B":
            your_play = Play.PAPER
        elif you == "C":
            your_play = Play.SCISSORS
        else:
            raise RuntimeError(f"Invalid input for opponent play '{you}'")

        if outcome_code == "X":
            outcome = GamePoints.LOSS
        elif outcome_code == "Y":
            outcome = GamePoints.DRAW
        elif outcome_code == "Z":
            outcome = GamePoints.WIN
        else:
            raise RuntimeError(f"Invalid input for outcome '{outcome_code}'")

        return your_play, outcome
