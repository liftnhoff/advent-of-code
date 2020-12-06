import pytest

from .stars import Sky


@pytest.fixture
def sky_fixture():
    yield Sky.from_file('day10/data/test_data.txt')


class TestSky:
    def test_from_file(self, sky_fixture):
        assert sky_fixture.stars[0].x == 9
        assert sky_fixture.stars[0].y == 1
        assert sky_fixture.stars[0].vx == 0
        assert sky_fixture.stars[0].vy == 2
        assert sky_fixture.stars[-1].x == -3
        assert sky_fixture.stars[-1].y == 6
        assert sky_fixture.stars[-1].vx == 2
        assert sky_fixture.stars[-1].vy == -1
