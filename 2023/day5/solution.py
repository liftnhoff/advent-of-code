from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class DestSourceRange:
    dest: int
    source: int
    range: int


@dataclass
class SourceBlock:
    dsr_index: int
    min: int
    max: int


class AlmanacMap:
    def __init__(self, dsr_values: list[DestSourceRange]):
        self.dsr_values = sorted(dsr_values, key=lambda x: x.source)

        self.source_blocks: list[SourceBlock] = []
        for index, dsr in enumerate(self.dsr_values):
            self.source_blocks.append(
                SourceBlock(index, dsr.source, dsr.source + dsr.range - 1)
            )

    def source_to_dest(self, source: int) -> int:
        search_blocks = self.source_blocks[:]
        while True:
            block_count = len(search_blocks)
            if block_count == 0:
                dest = source  # no mapping for this source value
                break
            middle_index = int((block_count - 1) / 2)
            middle_block = search_blocks[middle_index]
            if source < middle_block.min:
                search_blocks = search_blocks[:middle_index]
            elif source > middle_block.max:
                search_blocks = search_blocks[middle_index + 1 :]
            else:
                dsr = self.dsr_values[middle_block.dsr_index]
                dest = dsr.dest + (source - dsr.source)
                break

        return dest


@dataclass
class Almanac:
    seeds: tuple[int]
    maps: tuple[AlmanacMap]


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        almanac = self._load_almanac()
        locations = []
        for seed in almanac.seeds:
            source = seed
            for almanac_map in almanac.maps:
                source = almanac_map.source_to_dest(source)
            locations.append(source)

        return min(locations)

    def _load_almanac(self):
        seeds = tuple(int(v) for v in self.input_data[0][7:].split(" "))
        maps = []
        current_dsr_values = []
        for row in self.input_data[1:]:
            if "map" in row:
                if len(current_dsr_values) > 0:
                    maps.append(AlmanacMap(current_dsr_values))
                    current_dsr_values = []
            elif row:
                dsr = [int(v) for v in row.split(" ")]
                current_dsr_values.append(DestSourceRange(*dsr))

        if len(current_dsr_values) > 0:
            maps.append(AlmanacMap(current_dsr_values))

        return Almanac(seeds, tuple(maps))

    def part2(self):
        # This brute force approach doesn't work. A better way to do it is to reverse
        # the output map and be smart about the endpoints since everything is linear.
        # https://www.reddit.com/r/adventofcode/comments/18b4b0r/comment/kc3q9c6/

        almanac = self._load_almanac()
        min_location = 9e99
        for seed_start_index in range(0, len(almanac.seeds), 2):
            seed_start = almanac.seeds[seed_start_index]
            seed_range = almanac.seeds[seed_start_index + 1]
            for seed in range(seed_start, seed_start + seed_range):
                source = seed
                for almanac_map in almanac.maps:
                    source = almanac_map.source_to_dest(source)
                if source < min_location:
                    min_location = source

        return min_location
