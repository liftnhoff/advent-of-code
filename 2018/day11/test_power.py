import pytest

from .power import FuelGrid, Point


@pytest.fixture
def small_grid_fixture():
    # Example from https://en.wikipedia.org/wiki/Summed-area_table
    fuel_grid = FuelGrid(0)
    fuel_grid.MAX_INDEX = 6
    fuel_grid._power_grid = [
        [None] * 7,
        [None, 31, 2, 4, 33, 5, 36],
        [None, 12, 26, 9, 10, 29, 25],
        [None, 13, 17, 21, 22, 20, 18],
        [None, 24, 23, 15, 16, 14, 19],
        [None, 30, 8, 28, 27, 11, 7],
        [None, 1, 35, 34, 3, 32, 6],
    ]
    fuel_grid._build_summed_area_table()
    yield fuel_grid


class TestFuelGrid:
    def test_part1(self):
        serial_number = 8561
        size = 3
        fuel_grid = FuelGrid(serial_number)
        point, power = fuel_grid.find_highest_power_square(size)
        print(f'\n***** Day 11 Part 1 Answer: {point}')

    @pytest.mark.parametrize(
        'serial_number,size,expected', [
            (18, 3, (Point(33, 45), 29)),
            (42, 3, (Point(21, 61), 30)),
            (18, 16, (Point(90, 269), 113)),
            (42, 12, (Point(232, 251), 119)),
        ]
    )
    def test_find_highest_power_square(self, serial_number, size, expected):
        fuel_grid = FuelGrid(serial_number)
        point, power = fuel_grid.find_highest_power_square(size)
        assert point == expected[0]
        assert power == expected[1]

    def test__build_summed_area_table(self, small_grid_fixture):
        expected = [
            [0] * 7,
            [0, 31, 33, 37, 70, 75, 111],
            [0, 43, 71, 84, 127, 161, 222],
            [0, 56, 101, 135, 200, 254, 333],
            [0, 80, 148, 197, 278, 346, 444],
            [0, 110, 186, 263, 371, 450, 555],
            [0, 111, 222, 333, 444, 555, 666],
        ]
        assert small_grid_fixture._summed_area_table == expected

        expected = (
            small_grid_fixture._summed_area_table[3][2]
            + small_grid_fixture._summed_area_table[5][5]
            - small_grid_fixture._summed_area_table[5][2]
            - small_grid_fixture._summed_area_table[3][5]
        )
        assert expected == 111

    def test__calculate_square_power(self, small_grid_fixture):
        point = Point(1, 1)
        assert small_grid_fixture._calculate_square_power(point, 5) == 450

    @pytest.mark.parametrize(
        'serial_number,x_index,y_index,expected', [
            (8, 3, 5, 4),
            (57, 122, 79, -5),
            (39, 217, 196, 0),
            (71, 101, 153, 4),
        ]
    )
    def test_calculate_cell_power(self, serial_number, x_index, y_index, expected):
        fuel_grid = FuelGrid(serial_number)
        point = Point(x_index, y_index)
        assert fuel_grid.calculate_cell_power(point) == expected

    @pytest.mark.parametrize(
        'number,expected', [
            (12345, 3),
            (-987654321, 3),
            (1, 0),
            (10, 0),
            (99, 0),
            (100, 1),
            (-100, 1),
        ]
    )
    def test__hundreds_digit(self, number, expected):
        assert FuelGrid._hundreds_digit(number) == expected
