from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class RaceRecord:
    time: int
    distance: int


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        races = self._load_race_records()
        score = 1
        for race in races:
            score *= self._count_winning_possibilities(race)
        return score

    def _load_race_records(self) -> tuple[RaceRecord]:
        times = (int(v) for v in self.input_data[0][11:].split())
        distances = (int(v) for v in self.input_data[1][11:].split())
        return tuple(RaceRecord(t, d) for t, d in zip(times, distances))

    def _count_winning_possibilities(self, race: RaceRecord):
        # distance = v0 + t * v
        # 1 ht = 1 v
        win_possibilities = 0
        for speed in range(0, race.time + 1):
            distance = speed * (race.time - speed)
            if distance > race.distance:
                win_possibilities += 1

        return win_possibilities

    def part2(self):
        time = int("".join(self.input_data[0][11:].split()))
        distance = int("".join(self.input_data[1][11:].split()))
        return self._count_winning_possibilities(RaceRecord(time, distance))
