import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass(kw_only=True)
class GameRound:
    red: int = 0
    green: int = 0
    blue: int = 0


@dataclass
class Game:
    number: int
    rounds: list[GameRound]


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def _parser(row: str) -> Game:
            match = re.match(r"^Game (\d+): (.+)$", row)
            number = int(match.group(1))
            raw_rounds = match.group(2).split(";")
            rounds = []
            for raw_round in raw_rounds:
                count_by_color = {}
                for color_count in raw_round.strip().split(","):
                    count, color = color_count.strip().split(" ")
                    count_by_color[color] = int(count)
                rounds.append(GameRound(**count_by_color))

            return Game(number, rounds)

        return _parser

    def part1(self):
        red_max = 12
        green_max = 13
        blue_max = 14

        game_sum = 0
        for game in self.input_data:
            is_valid_game = True
            for round in game.rounds:
                if (
                    round.red > red_max
                    or round.green > green_max
                    or round.blue > blue_max
                ):
                    is_valid_game = False
                    break

            if is_valid_game:
                game_sum += game.number
        return game_sum

    def part2(self):
        game_power_sum = 0
        for game in self.input_data:
            red_max = 0
            green_max = 0
            blue_max = 0
            for round in game.rounds:
                if round.red > red_max:
                    red_max = round.red
                if round.green > green_max:
                    green_max = round.green
                if round.blue > blue_max:
                    blue_max = round.blue

            game_power_sum += red_max * green_max * blue_max

        return game_power_sum
