from collections import defaultdict


class MarbleCreationError(Exception):
    pass


class MarbleMania:
    PRIMARY_SCORE_MODULO = 23
    SECONDARY_SCORE_OFFSET = 7

    def __init__(self, player_count, final_marble_value):
        self.player_count = player_count
        self.final_marble_value = final_marble_value

        self.marble_count = final_marble_value + 1

    def play(self, print_circle=False):
        """Play a game of MarbleMania.

        Args:
            print_circle (bool): If True the circle of marbles will be printed
                at the end of each turn.

        Returns:
            (scores, first_marble): Tuple containing the scores of each player
                and the first marble of the circle.
        """
        scores = defaultdict(int)
        first_marble = Marble.create_first_marble()
        if print_circle:
            self._print_circle(first_marble)
        current_marble = first_marble
        for value in range(1, self.marble_count):
            if value % self.PRIMARY_SCORE_MODULO == 0:
                player_number = ((value - 1) % self.player_count) + 1
                offset_marble = current_marble
                for _ in range(self.SECONDARY_SCORE_OFFSET):
                    offset_marble = offset_marble.counter_cw_neighbor
                current_marble = offset_marble.cw_neighbor

                scores[player_number] += value + offset_marble.value
                offset_marble.remove()
            else:
                current_marble = current_marble.cw_neighbor.add_marble_cw(value)

            if print_circle:
                self._print_circle(first_marble)

        return scores, first_marble

    def _print_circle(self, first_marble):
        circle = self.build_circle(first_marble)
        print(', '.join(circle))

    def winning_score(self):
        scores, first_marble = self.play()
        return max(scores.values())

    @staticmethod
    def build_circle(first_marble):
        circle = []
        current_marble = first_marble
        while True:
            circle.append(str(current_marble.value))
            current_marble = current_marble.cw_neighbor
            if current_marble.value == first_marble.value:
                break

        return circle


class Marble:
    @classmethod
    def create_first_marble(cls):
        """Create the first Marble in the circle.

        Returns:
            Marble: The newly placed marble.
        """
        return cls(0, None, None)

    def __init__(self, value, cw_neighbor, counter_cw_neighbor):
        """Create a new Marble. New Marbles should only be created by the
        class method `create_first_marble` or instance methods `add_marble_cw`
        and `add_marble_counter_cw`.

        Args:
            value (int): The value of the Marble.
            cw_neighbor (Marble or None): The Marble next to this one in the
                clockwise direction. If None it is assumed this is the first
                Marble.
            counter_cw_neighbor (Marble or None): The Marble next to this one
                in the counter-clockwise direction. If None it is assumed this
                is the first Marble.
        """
        self.value = value

        if cw_neighbor is None or counter_cw_neighbor is None:
            if cw_neighbor is not None or counter_cw_neighbor is not None:
                raise(MarbleCreationError(
                    'There must be a Marble on both sides of a new Marble.'
                ))
            else:
                self.cw_neighbor = self
                self.counter_cw_neighbor = self
        else:
            self.cw_neighbor = cw_neighbor
            self.counter_cw_neighbor = counter_cw_neighbor

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'Marble {self.value}'

    def add_marble_cw(self, marble_value):
        """Create a marble and place it next to this marble in the clockwise
        direction.

        Args:
            marble_value (int): The value of the new marble.

        Returns:
            Marble: The newly placed marble.
        """
        new_marble = Marble(marble_value, self.cw_neighbor, self)
        self.cw_neighbor.counter_cw_neighbor = new_marble
        self.cw_neighbor = new_marble
        return new_marble

    def add_marble_counter_cw(self, marble_value):
        """Create a marble and place it next to this marble in the
        counter-clockwise direction.

        Args:
            marble_value (int): The value of the new marble.

        Returns:
            Marble: The newly placed marble.
        """
        new_marble = Marble(marble_value, self, self.counter_cw_neighbor)
        self.counter_cw_neighbor.cw_neighbor = new_marble
        self.counter_cw_neighbor = new_marble
        return new_marble

    def remove(self):
        """Remove a Marble from the circle."""
        self.cw_neighbor.counter_cw_neighbor = self.counter_cw_neighbor
        self.counter_cw_neighbor.cw_neighbor = self.cw_neighbor

        self.cw_neighbor = None
        self.counter_cw_neighbor = None
