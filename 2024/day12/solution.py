from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class GardenPlot:
    ri: int
    ci: int
    value: str
    edge_count: int | None

    def __eq__(self, other):
        if self.ri == other.ri and self.ci == other.ci:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.ri, self.ci))


class Solution(AdventOfCodeSolutionBase):
    def __init__(self, input_file: str):
        super().__init__(input_file)
        self.r_min = None
        self.r_max = None
        self.c_min = None
        self.c_max = None
        self.registered_plots = None

    def data_parser(self):
        return lambda x: x

    def part1(self):
        self.r_min, self.r_max = 0, len(self.input_data) - 1
        self.c_min, self.c_max = 0, len(self.input_data[0]) - 1
        self.registered_plots = set()

        regions = []
        for ri, row in enumerate(self.input_data):
            for ci, value in enumerate(row):
                region = self._fill_region(ri, ci, value)
                if region:
                    regions.append(region)

        price = 0
        for region in regions:
            area = 0
            edge_count = 0
            for gp in region:
                area += 1
                edge_count += gp.edge_count
            price += area * edge_count

        return price

    def _fill_region(self, ri, ci, region_value) -> list[GardenPlot]:
        plots_to_check = [GardenPlot(ri, ci, region_value, None)]
        region = []
        while plots_to_check:
            gp = plots_to_check.pop()
            if gp in self.registered_plots:
                continue

            edge_count = 0
            for ro in (-1, 1):
                if self._is_in_region(gp.ri + ro, gp.ci, region_value):
                    plots_to_check.append(
                        GardenPlot(gp.ri + ro, gp.ci, region_value, None)
                    )
                else:
                    edge_count += 1

            for co in (-1, 1):
                if self._is_in_region(gp.ri, gp.ci + co, region_value):
                    plots_to_check.append(
                        GardenPlot(gp.ri, gp.ci + co, region_value, None)
                    )
                else:
                    edge_count += 1

            gp.edge_count = edge_count
            region.append(gp)
            self.registered_plots.add(gp)

        return region

    def _is_in_region(self, ri, ci, region_value) -> bool:
        return (
            self.r_min <= ri <= self.r_max
            and self.c_min <= ci <= self.c_max
            and self.input_data[ri][ci] == region_value
        )

    def part2(self):
        pass
        # self.r_min, self.r_max = 0, len(self.input_data) - 1
        # self.c_min, self.c_max = 0, len(self.input_data[0]) - 1
        # self.registered_plots = set()
        #
        # regions = []
        # for ri, row in enumerate(self.input_data):
        #     for ci, value in enumerate(row):
        #         region = self._fill_region(ri, ci, value)
        #         if region:
        #             regions.append(region)
        #
        # # for region in regions:
        # #     region_set = set(region)
        # #     edges = set()
        # #     for ri, row in enumerate(self.input_data):
        # #         in_region = False
        # #         for ci, value in enumerate(row):
        # #             gp = GardenPlot(ri, ci, value, None)
        # #             if gp in region_set:
        # #                 if not in_region:
        # #                     edges.add((ri, ci))
        # #                     in_region = True
        # #             else:
        # #                 if in_region:
        # #                     edges.add((ri, ci))
        # #                     in_region = False
        # #         if in_region:
        # #             edges.add((ri, self.c_max + 1))
        # #
        # #     print(region)
        # #     print(edges)
        #
        # corner_count = 0  # the number of corners == number of sides
        # counted_gp = set()
        # for region in regions:
        #     region_set = set(region)
        #     for gp in region:
        #         if gp.edge_count == 4:
        #             corner_count += 4
        #             counted_gp.add(gp)
        #         elif gp.edge_count == 3:
        #             # check if diagonals have edge
        #             corner_count += 2
        #             for (ro, co) in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
        #                 # if self._is_in_region(gp.ri + ro, gp.ci + co, gp.value):
        #         elif gp.edge_count == 2:
        #
        #         for ro in (-1, 1):
        #             if self._is_in_region(gp.ri + ro, gp.ci, gp.value):
        #                 plots_to_check.append(
        #                     GardenPlot(gp.ri + ro, gp.ci, region_value, None)
        #                 )
        #             else:
        #                 edge_count += 1
        #
        # price = 0
        # for region in regions:
        #     area = 0
        #     edge_count = 0
        #     for gp in region:
        #         area += 1
        #         edge_count += gp.edge_count
        #     price += area * edge_count
        #
        # return price
