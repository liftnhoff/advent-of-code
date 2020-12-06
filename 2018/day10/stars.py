from dataclasses import dataclass
from itertools import count
import re


@dataclass
class Star:
    x: int
    y: int
    vx: int
    vy: int


class Sky:
    STAR_REGEX = re.compile(
        r'^position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>$'
    )

    def __init__(self, stars):
        """
        Args:
            stars (list[Star]): The initial collection of Stars.
        """
        self.stars = stars

    @classmethod
    def from_file(cls, datafile):
        with open(datafile) as fid:
            stars = []
            for line in fid:
                match = cls.STAR_REGEX.match(line)
                stars.append(
                    Star(
                        int(match.group(1)),
                        int(match.group(2)),
                        int(match.group(3)),
                        int(match.group(4)),
                    )
                )

        return cls(stars)

    def find_message(self):
        prev_area = self._area(0)
        for step in count():
            current_area = self._area(step)
            if current_area > prev_area:
                print(f'Smallest area found at step {step - 1}. Area = {prev_area}')
                self._display(step - 1)
                break
            prev_area = current_area

    def _area(self, step):
        x_pos, y_pos = self._positions(step)
        return (max(x_pos) - min(x_pos)) * (max(y_pos) - min(y_pos))

    def _positions(self, step):
        x_pos = []
        y_pos = []
        for star in self.stars:
            x_pos.append(star.x + step * star.vx)
            y_pos.append(star.y + step * star.vy)

        return x_pos, y_pos

    def _display(self, step):
        x_pos, y_pos = self._positions(step)
        points = set(zip(x_pos, y_pos))

        min_x = min(x_pos)
        max_x = max(x_pos)
        min_y = min(y_pos)
        max_y = max(y_pos)

        rows = []
        for y in range(min_y, max_y + 1):
            row = []
            for x in range(min_x, max_x + 1):
                if (x, y) in points:
                    row.append('#')
                else:
                    row.append(' ')
            rows.append(''.join(row))
        print('\n'.join(rows))
