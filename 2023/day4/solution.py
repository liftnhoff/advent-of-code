import re
from collections import deque
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class ScratchCard:
    id: int
    winning_numbers: set[int]
    card_numbers: set[int]


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def _parser(row: str) -> ScratchCard:
            match = re.match(r"^Card +(\d+): ([0-9 ]+) \| ([0-9 ]+)$", row)
            return ScratchCard(
                int(match.group(1)),
                {int(x) for x in match.group(2).split(" ") if x.strip()},
                {int(x) for x in match.group(3).split(" ") if x.strip()},
            )

        return _parser

    def part1(self):
        points = 0
        for card in self.input_data:
            winning_count = len(card.winning_numbers.intersection(card.card_numbers))
            if winning_count > 0:
                points += 1 * (2 ** (winning_count - 1))

        return points

    def part2(self):
        max_card_id = self.input_data[-1].id
        cards_by_id = {card.id: card for card in self.input_data}
        card_queue = deque(self.input_data)

        card_count = 0
        while len(card_queue) > 0:
            card_count += 1
            card = card_queue.popleft()
            winning_count = len(card.winning_numbers.intersection(card.card_numbers))
            for index in range(winning_count):
                if index <= max_card_id:
                    card_queue.append(cards_by_id[card.id + index + 1])

        return card_count
