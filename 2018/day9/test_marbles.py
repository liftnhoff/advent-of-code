import pytest

from .marbles import Marble, MarbleCreationError, MarbleMania


class TestMarbleMania:
    def test_part1(self):
        game = MarbleMania(430, 71588)
        print(f'\n***** Day 9 Part 1 Answer: {game.winning_score()}')

    @pytest.mark.slow
    def test_part2(self):
        game = MarbleMania(430, 7158800)
        print(f'\n***** Day 9 Part 1 Answer: {game.winning_score()}')

    @pytest.mark.parametrize(
        'player_count,final_marble_value,expected,missing_marbles', [
            (9, 25, 32, 2),
            (10, 1618, 8317, 140),
            (13, 7999, 146373, 694),
            (17, 1104, 2764, 96),
            (21, 6111, 54718, 530),
            (30, 5807, 37305, 504),
        ]
    )
    def test_play(self, player_count, final_marble_value, expected, missing_marbles):
        game = MarbleMania(player_count, final_marble_value)
        scores, first_marble = game.play(print_circle=False)
        assert max(scores.values()) == expected

        circle = game.build_circle(first_marble)
        assert len(circle) == (final_marble_value + 1) - missing_marbles

class TestMarble:
    def test__init__(self):
        marble0 = Marble(0, None, None)
        with pytest.raises(MarbleCreationError):
            Marble(0, None, marble0)

        with pytest.raises(MarbleCreationError):
            Marble(0, marble0, None)
