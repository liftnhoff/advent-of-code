import pytest


from .points import Point, PointCollection


@pytest.fixture
def point_fixture():
    yield Point(1, 4, 7)


class TestPoint:
    def test_manhattan_distance(self, point_fixture):
        origin_distance = point_fixture.row_index + point_fixture.col_index
        assert point_fixture.manhattan_distance(0, 0) == origin_distance

        assert point_fixture.manhattan_distance(
            point_fixture.row_index,
            point_fixture.col_index
        ) == 0


@pytest.fixture
def points_fixture():
    points = PointCollection()
    yield points


class TestPointCollection:
    def test_match_example_solution_part1(self):
        points = PointCollection.read_points_file('day6/data/test_data.txt')
        largest_point = points.point_with_largest_finite_span()
        assert largest_point.span_size == 17

    def test_match_example_solution_part2(self):
        points = PointCollection.read_points_file('day6/data/test_data.txt')
        limit = 32
        area = points.area_of_region_near_all_points(limit)
        assert area == 16

    def test_add_point(self, points_fixture, point_fixture):
        points_fixture.add_point(point_fixture)
        assert len(points_fixture._points) == 1
        assert points_fixture.min_row_index == 0
        assert points_fixture.max_row_index == point_fixture.row_index
        assert points_fixture.min_col_index == 0
        assert points_fixture.max_col_index == point_fixture.col_index

    def test_add_point_wrong_type(self, points_fixture):
        with pytest.raises(TypeError):
            points_fixture.add_point(1)

    def test__closest_point(self, points_fixture):
        points_fixture.add_point(Point(1, 1, 1))
        points_fixture.add_point(Point(2, 50, 50))

        result = points_fixture._closest_point(2, 2)
        assert result.number == 1

        result = points_fixture._closest_point(49, 49)
        assert result.number == 2

        result = points_fixture._closest_point(25, 26)
        assert result is None  # Equidistant

    def test__get_largest_finite_span_point(self, points_fixture):
        point = Point(1, 1, 1)
        point.span_size = 10
        point.span_touches_edge = True
        points_fixture.add_point(point)
        point = Point(2, 1, 1)
        point.span_size = 5
        point.span_touches_edge = False
        points_fixture.add_point(point)
        point = Point(3, 1, 1)
        point.span_size = 3
        point.span_touches_edge = False
        points_fixture.add_point(point)

        result = points_fixture._get_largest_finite_span_point()
        assert result.number == 2
