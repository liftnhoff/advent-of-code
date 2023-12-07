from collections import Counter
from enum import IntEnum

from base.solution import AdventOfCodeSolutionBase


class CardLabels(IntEnum):
    C_A = 14
    C_K = 13
    C_Q = 12
    C_J = 11
    C_T = 10
    C_9 = 9
    C_8 = 8
    C_7 = 7
    C_6 = 6
    C_5 = 5
    C_4 = 4
    C_3 = 3
    C_2 = 2


class HandTypes(IntEnum):
    FIVE_KIND = 70
    FOUR_KIND = 60
    FULL_HOUSE = 50
    THREE_KIND = 40
    TWO_PAIR = 30
    ONE_PAIR = 20
    HIGH_CARD = 10


class CardHand:
    def __init__(self, raw_cards: str, bid: int):
        self.raw_cards = raw_cards
        self.bid = bid

        self.cards = tuple(CardLabels[f"C_{raw_card}"] for raw_card in raw_cards)

        counts = Counter(raw_cards).most_common()
        if len(counts) == 1:
            self.type = HandTypes.FIVE_KIND
        elif len(counts) == 2:
            if counts[0][1] == 4:
                self.type = HandTypes.FOUR_KIND
            elif counts[0][1] == 3:
                self.type = HandTypes.FULL_HOUSE
            else:
                raise RuntimeError(f"Invalid hand type: {counts}")
        elif len(counts) == 3:
            if counts[0][1] == 3:
                self.type = HandTypes.THREE_KIND
            elif counts[0][1] == 2:
                self.type = HandTypes.TWO_PAIR
            else:
                raise RuntimeError(f"Invalid hand type: {counts}")
        elif len(counts) == 4:
            self.type = HandTypes.ONE_PAIR
        elif len(counts) == 5:
            self.type = HandTypes.HIGH_CARD
        else:
            raise RuntimeError(f"Invalid hand type: {counts}")

    def __repr__(self):
        cards_str = ",".join(c.name for c in self.cards)
        return f"{self.raw_cards} {self.bid} {cards_str} {self.type.name}"

    def __lt__(self, other):
        if self.type is other.type:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card < other_card:
                    return True
                elif self_card > other_card:
                    return False
            return False
        else:
            return self.type < other.type


class CardLabelsWild(IntEnum):
    C_A = 14
    C_K = 13
    C_Q = 12
    C_T = 10
    C_9 = 9
    C_8 = 8
    C_7 = 7
    C_6 = 6
    C_5 = 5
    C_4 = 4
    C_3 = 3
    C_2 = 2
    C_J = 1


class CardHandWild:
    def __init__(self, raw_cards: str, bid: int):
        self.raw_cards = raw_cards
        self.bid = bid

        self.cards = tuple(CardLabelsWild[f"C_{raw_card}"] for raw_card in raw_cards)

        wild = "J"
        card_counts = Counter(raw_cards)
        wild_count = card_counts.get(wild, 0)
        counts = card_counts.most_common()
        counts = [list(x) for x in counts if x[0] != wild]
        if len(counts) == 0:
            self.type = HandTypes.FIVE_KIND  # all wild cards
        else:
            counts[0][1] += wild_count
            if len(counts) == 1:
                self.type = HandTypes.FIVE_KIND
            elif len(counts) == 2:
                if counts[0][1] == 4:
                    self.type = HandTypes.FOUR_KIND
                elif counts[0][1] == 3:
                    self.type = HandTypes.FULL_HOUSE
                else:
                    raise RuntimeError(f"Invalid hand type: {counts}")
            elif len(counts) == 3:
                if counts[0][1] == 3:
                    self.type = HandTypes.THREE_KIND
                elif counts[0][1] == 2:
                    self.type = HandTypes.TWO_PAIR
                else:
                    raise RuntimeError(f"Invalid hand type: {counts}")
            elif len(counts) == 4:
                self.type = HandTypes.ONE_PAIR
            elif len(counts) == 5:
                self.type = HandTypes.HIGH_CARD
            else:
                raise RuntimeError(f"Invalid hand type: {counts}")

    def __repr__(self):
        cards_str = ",".join(c.name for c in self.cards)
        return f"{self.raw_cards} {self.bid} {cards_str} {self.type.name}"

    def __lt__(self, other):
        if self.type is other.type:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card < other_card:
                    return True
                elif self_card > other_card:
                    return False
            return False
        else:
            return self.type < other.type


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        hands = []
        for row in self.input_data:
            cards, bid = row.split()
            hands.append(CardHand(cards, int(bid)))

        score = 0
        sorted_hands = sorted(hands)
        for rank, card_hand in enumerate(sorted_hands, 1):
            score += rank * card_hand.bid
        return score

    def part2(self):
        hands = []
        for row in self.input_data:
            cards, bid = row.split()
            hands.append(CardHandWild(cards, int(bid)))

        score = 0
        sorted_hands = sorted(hands)
        for rank, card_hand in enumerate(sorted_hands, 1):
            score += rank * card_hand.bid
        return score
