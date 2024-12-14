import re

import numpy

# import matplotlib.pyplot as plt

from base.solution import AdventOfCodeSolutionBase


class Robot:
    # R_SIZE = 7  # test values
    # C_SIZE = 11
    R_SIZE = 103  # real values
    C_SIZE = 101

    def __init__(self, ri, ci, rv, cv):
        self.ri = ri
        self.ci = ci
        self.rv = rv
        self.cv = cv

    def __str__(self):
        return f"Robot({self.ri},{self.ci},{self.rv},{self.cv})"

    def __repr__(self):
        return str(self)

    def move(self):
        self.ri = (self.ri + self.rv) % self.R_SIZE
        self.ci = (self.ci + self.cv) % self.C_SIZE


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        def _parser(line):
            match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            return Robot(
                int(match.group(2)),
                int(match.group(1)),
                int(match.group(4)),
                int(match.group(3)),
            )

        return _parser

    def part1(self):
        step_count = 100
        for _ in range(step_count):
            for robot in self.input_data:
                robot.move()

        quadrant_counts = [0] * 4
        r_mid = Robot.R_SIZE // 2
        c_mid = Robot.C_SIZE // 2
        for robot in self.input_data:
            if 0 <= robot.ri < r_mid and 0 <= robot.ci < c_mid:
                quadrant_counts[0] += 1
            elif 0 <= robot.ri < r_mid and c_mid < robot.ci < Robot.C_SIZE:
                quadrant_counts[1] += 1
            elif r_mid < robot.ri < Robot.R_SIZE and 0 <= robot.ci < c_mid:
                quadrant_counts[2] += 1
            elif r_mid < robot.ri < Robot.R_SIZE and c_mid < robot.ci < Robot.C_SIZE:
                quadrant_counts[3] += 1

        score = 1
        for qc in quadrant_counts:
            score *= qc

        return score

    def part2(self):
        r_mid = Robot.R_SIZE // 2
        c_mid = Robot.C_SIZE // 2

        step_count = 10000
        heuristic = []
        tree_step_count = None
        for index in range(1, step_count):
            dist = []
            for robot in self.input_data:
                robot.move()
                dist.append(abs(robot.ri - r_mid) + abs(robot.ci - c_mid))

            heuristic.append(numpy.mean(dist))

            if numpy.mean(dist) < 35:
                # xx = []
                # yy = []
                # for robot in self.input_data:
                #     xx.append(robot.ci)
                #     yy.append(robot.ri)
                # plt.plot(xx, yy, ".", linestyle="None")
                # plt.show()

                tree_step_count = index
                break

        # plt.plot(heuristic)
        # plt.show()

        return tree_step_count
