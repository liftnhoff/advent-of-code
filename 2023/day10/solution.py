import math
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum

from base.solution import AdventOfCodeSolutionBase


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Position:
    def __init__(self, row_index: int, col_index: int):
        self.row_index = row_index
        self.col_index = col_index

    def step_in_direction(self, direction: Direction):
        if direction is Direction.UP:
            return Position(self.row_index - 1, self.col_index)
        elif direction is Direction.DOWN:
            return Position(self.row_index + 1, self.col_index)
        elif direction is Direction.LEFT:
            return Position(self.row_index, self.col_index - 1)
        elif direction is Direction.RIGHT:
            return Position(self.row_index, self.col_index + 1)
        else:
            raise ValueError(f"Invalid direction {direction}")

    def __repr__(self):
        return f"Position({self.row_index}, {self.col_index})"


@dataclass
class PipeNode:
    shape: str
    position: Position
    distance_from_start: int
    in_dir: Direction

    def __hash__(self):
        return hash((self.position.row_index, self.position.col_index))


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        node = self._find_start_pipe()
        seen_nodes = [node]
        while True:
            node = self._next_node(node)
            if node.shape == "S":
                break
            seen_nodes.append(node)

        return math.ceil(len(seen_nodes) / 2)

    def _find_start_pipe(self) -> PipeNode:
        sr = None
        sc = None
        for row_index, row in enumerate(self.input_data):
            for col_index, value in enumerate(row):
                if value == "S":
                    sr = row_index
                    sc = col_index
                    break

        # possible {"|", "-", "L", "J", "7", "F", "."}
        if sr - 1 < 0 or self.input_data[sr - 1][sc] in {"-", "L", "J", "."}:
            # doesn't connect to top, in {"-", "7", "F"}
            if sc + 1 > len(self.input_data[0]) or self.input_data[sr][sc + 1] in {
                "|",
                "L",
                "F",
                ".",
            }:
                # doesn't connect to right, must be "7"
                start_node = PipeNode("7", Position(sr, sc), 0, Direction.RIGHT)
            else:
                # connects to right, in {"-", "F"}
                if sr + 1 > len(self.input_data) or self.input_data[sr + 1][sc] in {
                    "-",
                    "7",
                    "F",
                    ".",
                }:
                    # doesn't connect down, is "-"
                    start_node = PipeNode("-", Position(sr, sc), 0, Direction.RIGHT)
                else:
                    # connects down, is "F"
                    start_node = PipeNode("F", Position(sr, sc), 0, Direction.UP)
        else:
            # connects to top, in {"|", "L", "J"}
            if sc + 1 > len(self.input_data[0]) or self.input_data[sr][sc + 1] in {
                "|",
                "L",
                "F",
                ".",
            }:
                # doesn't connect to right, must be in {"|", "J"}
                if sr + 1 > len(self.input_data) or self.input_data[sr + 1][sc] in {
                    "-",
                    "7",
                    "F",
                    ".",
                }:
                    # doesn't connect down, is "J"
                    start_node = PipeNode("J", Position(sr, sc), 0, Direction.DOWN)
                else:
                    # connects down, is "|"
                    start_node = PipeNode("|", Position(sr, sc), 0, Direction.DOWN)
            else:
                # connects right, is "L"
                start_node = PipeNode("L", Position(sr, sc), 0, Direction.LEFT)

        return start_node

    def _next_node(self, node: PipeNode) -> PipeNode:
        if node.shape == "|":
            if node.in_dir is Direction.DOWN:
                out_dir = Direction.DOWN
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.UP
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
        elif node.shape == "-":
            if node.in_dir is Direction.RIGHT:
                out_dir = Direction.RIGHT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.LEFT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
        elif node.shape == "L":
            if node.in_dir is Direction.DOWN:
                out_dir = Direction.RIGHT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.UP
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
        elif node.shape == "J":
            if node.in_dir is Direction.DOWN:
                out_dir = Direction.LEFT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.UP
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
        elif node.shape == "7":
            if node.in_dir is Direction.RIGHT:
                out_dir = Direction.DOWN
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.LEFT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
        elif node.shape == "F":
            if node.in_dir is Direction.UP:
                out_dir = Direction.RIGHT
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )
            else:
                out_dir = Direction.DOWN
                new_pos = node.position.step_in_direction(out_dir)
                return PipeNode(
                    self.input_data[new_pos.row_index][new_pos.col_index],
                    new_pos,
                    node.distance_from_start + 1,
                    out_dir,
                )

        raise ValueError("Invalid node incoming direction")

    def part2(self):
        node = self._find_start_pipe()
        seen_nodes = [node]
        while True:
            node = self._next_node(node)
            if node.shape == "S":
                break
            seen_nodes.append(node)

        # draw a horizontal line and count walls intersections.
        node_cols_by_row = defaultdict(set)
        for node in seen_nodes:
            node_cols_by_row[node.position.row_index].add(node.position.col_index)

        in_count = 0
        empty_set = set()
        for row_index, row in enumerate(self.input_data):
            is_counting = False
            for col_index, value in enumerate(row):
                if col_index in node_cols_by_row.get(row_index, empty_set):
                    if value == "S":
                        value = seen_nodes[0].shape

                    if value == "|" or value == "J" or value == "L":
                        is_counting = not is_counting
                else:
                    if is_counting:
                        in_count += 1

        return in_count
