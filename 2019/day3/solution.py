from base.solution import AdventOfCodeSolutionBase

from dataclasses import dataclass


@dataclass
class Pos:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x.split(',')

    def part1(self):
        wire1 = build_wire(self.input_data[0])
        wire2 = build_wire(self.input_data[1])

        intersections = set(wire1).intersection(wire2)
        intersection_and_dist = []
        for pos in intersections:
            intersection_and_dist.append((pos, cartesian_distance(pos.x, pos.y, 0, 0)))

        min_dist = sorted(intersection_and_dist, key=lambda x: x[1])[1][1]
        return min_dist

    def part2(self):
        wire1 = build_wire(self.input_data[0])
        wire2 = build_wire(self.input_data[1])

        intersections = set(wire1).intersection(wire2)
        intersections.discard(Pos(0, 0))
        closest_dist = 9999999999
        for intersection in intersections:
            dist = wire1.index(intersection) + wire2.index(intersection)
            if dist < closest_dist:
                closest_dist = dist

        return closest_dist


def build_wire(steps: list[str]) -> list[Pos]:
    wire = [Pos(0, 0)]
    for step in steps:
        dir = step[0]
        amount = int(step[1:])
        if dir == 'U':
            for _ in range(amount):
                wire.append(
                    Pos(wire[-1].x, wire[-1].y + 1)
                )
        elif dir == 'D':
            for _ in range(amount):
                wire.append(
                    Pos(wire[-1].x, wire[-1].y - 1)
                )
        elif dir == 'L':
            for _ in range(amount):
                wire.append(
                    Pos(wire[-1].x - 1, wire[-1].y)
                )
        elif dir == 'R':
            for _ in range(amount):
                wire.append(
                    Pos(wire[-1].x + 1, wire[-1].y)
                )

    return wire


def cartesian_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

