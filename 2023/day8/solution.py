import math
import re
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class Node:
    name: str
    left_node_name: str
    right_node_name: str


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        return None
        directions = self.input_data[0]
        nodes_by_name = self._load_nodes_by_name()
        node = nodes_by_name["AAA"]
        step_count = 0
        while True:
            if node.name == "ZZZ":
                break

            for direction in directions:
                step_count += 1
                if direction == "L":
                    node = nodes_by_name[node.left_node_name]
                else:
                    node = nodes_by_name[node.right_node_name]

                if node.name == "ZZZ":
                    break

        return step_count

    def _load_nodes_by_name(self) -> dict[str, Node]:
        nodes_by_name = {}
        pattern = re.compile(r"^(\w{3}) = \((\w{3}), (\w{3})\)$")
        for line in self.input_data[2:]:
            match = pattern.match(line)
            node = Node(match.group(1), match.group(2), match.group(3))
            nodes_by_name[node.name] = node

        return nodes_by_name

    def part2(self):
        # Assume that since we're going around the loops a bunch of times that there is
        # some easy way to guess the LCM and that's the answer:
        # https://www.reddit.com/r/adventofcode/comments/18dfpub/2023_day_8_part_2_why_is_spoiler_correct/
        directions = self.input_data[0]
        nodes_by_name = self._load_nodes_by_name()

        current_nodes = []
        for name, node in nodes_by_name.items():
            if name[2] == "A":
                current_nodes.append(node)
        step_counts = [0] * len(current_nodes)
        while not all(node.name[2] == "Z" for node in current_nodes):
            for direction in directions:
                for index, node in enumerate(current_nodes[:]):
                    if node.name[2] == "Z":
                        continue

                    step_counts[index] += 1
                    if direction == "L":
                        current_nodes[index] = nodes_by_name[node.left_node_name]
                    else:
                        current_nodes[index] = nodes_by_name[node.right_node_name]

        return math.lcm(*step_counts)

        # brute force below, takes a long time
        directions = self.input_data[0]
        nodes_by_name = self._load_nodes_by_name()
        step_count = 0

        current_nodes = []
        for name, node in nodes_by_name.items():
            if name[2] == "A":
                current_nodes.append(node)

        while True:
            if all(node.name[2] == "Z" for node in current_nodes):
                break

            for direction in directions:
                step_count += 1
                for index, node in enumerate(current_nodes):
                    if direction == "L":
                        current_nodes[index] = nodes_by_name[node.left_node_name]
                    else:
                        current_nodes[index] = nodes_by_name[node.right_node_name]

                if all(node.name[2] == "Z" for node in current_nodes):
                    break

        return step_count
