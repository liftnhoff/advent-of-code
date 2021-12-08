from typing import Generic, Optional, TypeVar

from base.solution import AdventOfCodeSolutionBase

LanternFishType = TypeVar("LanternFishType")


class LanternFishSchool:
    def __init__(self, offspring_timers: list[int]):
        self.fishes = [LanternFish(timer) for timer in offspring_timers]

    def update_fish_timers(self):
        new_fishies = []
        for fish in self.fishes:
            new_fish = fish.update_timer_and_maybe_spawn_new_fish()
            if new_fish:
                new_fishies.append(new_fish)

        self.fishes.extend(new_fishies)

    def count(self) -> int:
        return len(self.fishes)


class LanternFish(Generic[LanternFishType]):
    _OFFSPRING_TIMER_START = 6
    _NEW_FISH_OFFSPRING_DELAY = 2

    def __init__(self, offspring_timer: int):
        self.offspring_timer = offspring_timer

    def update_timer_and_maybe_spawn_new_fish(self) -> Optional[LanternFishType]:
        self.offspring_timer -= 1
        if self.offspring_timer < 0:
            self.offspring_timer = self._OFFSPRING_TIMER_START
            return LanternFish(
                self._OFFSPRING_TIMER_START + self._NEW_FISH_OFFSPRING_DELAY
            )

        return None


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: [int(v) for v in x.split(",") if x]

    def part1(self):
        fish_school = LanternFishSchool(self.input_data[0])
        for _ in range(80):
            fish_school.update_fish_timers()

        return fish_school.count()

    def part2(self):
        fish_school = AggregatedLanternFishSchool(self.input_data[0])
        for _ in range(256):
            fish_school.update_fish_timers()

        return fish_school.count()


class AggregatedLanternFishSchool:
    """
    Note this works for part 1 as well. It is about 5000x faster for 80 days and won't
    run out of memory for high day values.
    """

    _OFFSPRING_TIMER_START = 6
    _NEW_FISH_OFFSPRING_DELAY = 2

    def __init__(self, offspring_timers: list[int]):
        self.timer_counts = self._get_empty_timer_counts()
        for timer_value in offspring_timers:
            self.timer_counts[timer_value] += 1

    def _get_empty_timer_counts(self) -> dict[int, int]:
        return {
            t: 0
            for t in range(
                self._OFFSPRING_TIMER_START + self._NEW_FISH_OFFSPRING_DELAY + 1
            )
        }

    def update_fish_timers(self):
        new_timer_counts = self._get_empty_timer_counts()
        for timer_value, count in self.timer_counts.items():
            new_timer_counts[timer_value - 1] = count

        spawn_count = new_timer_counts.pop(-1, 0)
        new_timer_counts[self._OFFSPRING_TIMER_START] += spawn_count
        new_timer_counts[
            self._OFFSPRING_TIMER_START + self._NEW_FISH_OFFSPRING_DELAY
        ] += spawn_count

        self.timer_counts = new_timer_counts

    def count(self) -> int:
        return sum(self.timer_counts.values())
