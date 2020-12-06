from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


class FuelGrid:
    MIN_INDEX = 1
    MAX_INDEX = 300
    RACK_ID_OFFSET = 10

    def __init__(self, serial_number):
        self.serial_number = serial_number

        self._power_grid = None
        self._summed_area_table = None

    def find_highest_power_of_all_squares(self):
        results = []
        for size in range(1, self._grid_size):
            print(f'Checking squares of size {size}')
            point, power = self.find_highest_power_square(size)
            results.append((size, point, power))

        return max(results, key=lambda x: x[2])

    def find_highest_power_square(self, size):
        """Find the square with the highest power density in the FuelGrid.

        Args:
            size(int): The size of square that should be checked.

        Returns:
            tuple(Point, int): The top-left coordinates of the square with the highest
                power level in the grid, and the power level in that square.
        """
        self._build_summed_area_table()
        max_power_point = None
        max_power = -1e30
        for top_left_y_index in range(self.MIN_INDEX, self.MAX_INDEX - size + 1):
            for top_left_x_index in range(self.MIN_INDEX, self.MAX_INDEX - size + 1):
                point = Point(top_left_x_index, top_left_y_index)
                power = self._calculate_square_power(point, size)
                if power > max_power:
                    max_power_point = point
                    max_power = power

        return max_power_point, max_power

    def _build_summed_area_table(self):
        if self._summed_area_table is not None:
            return

        self._build_power_grid()

        # Pad the grid with and extra row and column of `0`s to account for
        # 1-indexing.
        self._summed_area_table = [[0] * (self._grid_size + 1)]
        for y_index in range(self.MIN_INDEX, self.MAX_INDEX + 1):
            self._summed_area_table.append([0] * (self._grid_size + 1))
            for x_index in range(self.MIN_INDEX, self.MAX_INDEX + 1):
                self._summed_area_table[y_index][x_index] = (
                    self._power_grid[y_index][x_index]
                    + self._summed_area_table[y_index - 1][x_index]
                    + self._summed_area_table[y_index][x_index - 1]
                    - self._summed_area_table[y_index - 1][x_index - 1]
                )

    def _build_power_grid(self):
        if self._power_grid is not None:
            return

        # Pad the grid with and extra row and column of `None` to account for
        # 1-indexing.
        self._power_grid = [[None] * (self._grid_size + 1)]
        for y_index in range(self.MIN_INDEX, self.MAX_INDEX + 1):
            self._power_grid.append([None] * (self._grid_size + 1))
            for x_index in range(self.MIN_INDEX, self.MAX_INDEX + 1):
                point = Point(x_index, y_index)
                self._power_grid[y_index][x_index] = self.calculate_cell_power(point)

    @property
    def _grid_size(self):
        return self.MAX_INDEX - self.MIN_INDEX + 1

    def _calculate_square_power(self, top_left_point, size):
        # power_level = 0
        # for yi in range(top_left_point.y, top_left_point.y + size):
        #     for xi in range(top_left_point.x, top_left_point.x + size):
        #         power_level += self._power_grid[yi][xi]
        power_level = (
            self._summed_area_table[top_left_point.y - 1][top_left_point.x - 1]
            + self._summed_area_table[top_left_point.y + size - 1][top_left_point.x + size - 1]
            - self._summed_area_table[top_left_point.y + size - 1][top_left_point.x - 1]
            - self._summed_area_table[top_left_point.y - 1][top_left_point.x + size - 1]
        )
        return power_level

    def calculate_cell_power(self, point):
        """
        Args:
            point (Point): Coordinates of the cell.

        Returns:
            int: Power level for the cell.
        """
        rack_id = point.x + self.RACK_ID_OFFSET
        power_level = (rack_id * point.y + self.serial_number) * rack_id
        power_level = self._hundreds_digit(power_level) - 5
        return power_level

    @staticmethod
    def _hundreds_digit(number):
        return abs(number) // 100 % 10
