from collections import deque

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        warehouse, robot_pos, moves = self._load_warehouse_and_robot()
        robot_ri, robot_ci = robot_pos
        # <^^>>>vv<v>>v<<
        for move in moves:
            pending_moves = []
            if move == "^":
                mr = robot_ri - 1
                pending_moves.append(mr)
                next_value = warehouse[mr][robot_ci]
                while next_value == "O":
                    mr -= 1
                    pending_moves.append(mr)
                    next_value = warehouse[mr][robot_ci]

                mr = pending_moves[-1]
                next_pos = warehouse[mr][robot_ci]
                if next_pos == ".":
                    for mr in reversed(pending_moves):
                        warehouse[mr][robot_ci] = warehouse[mr + 1][robot_ci]
                    warehouse[robot_ri][robot_ci] = "."
                    robot_ri -= 1
            elif move == "v":
                mr = robot_ri + 1
                pending_moves.append(mr)
                next_value = warehouse[mr][robot_ci]
                while next_value == "O":
                    mr += 1
                    pending_moves.append(mr)
                    next_value = warehouse[mr][robot_ci]

                mr = pending_moves[-1]
                next_pos = warehouse[mr][robot_ci]
                if next_pos == ".":
                    for mr in reversed(pending_moves):
                        warehouse[mr][robot_ci] = warehouse[mr - 1][robot_ci]
                    warehouse[robot_ri][robot_ci] = "."
                    robot_ri += 1
            elif move == "<":
                mc = robot_ci - 1
                pending_moves.append(mc)
                next_value = warehouse[robot_ri][mc]
                while next_value == "O":
                    mc -= 1
                    pending_moves.append(mc)
                    next_value = warehouse[robot_ri][mc]

                mc = pending_moves[-1]
                next_pos = warehouse[robot_ri][mc]
                if next_pos == ".":
                    for mc in reversed(pending_moves):
                        warehouse[robot_ri][mc] = warehouse[robot_ri][mc + 1]
                    warehouse[robot_ri][robot_ci] = "."
                    robot_ci -= 1
            elif move == ">":
                mc = robot_ci + 1
                pending_moves.append(mc)
                next_value = warehouse[robot_ri][mc]
                while next_value == "O":
                    mc += 1
                    pending_moves.append(mc)
                    next_value = warehouse[robot_ri][mc]

                mc = pending_moves[-1]
                next_pos = warehouse[robot_ri][mc]
                if next_pos == ".":
                    for mc in reversed(pending_moves):
                        warehouse[robot_ri][mc] = warehouse[robot_ri][mc - 1]
                    warehouse[robot_ri][robot_ci] = "."
                    robot_ci += 1

            # print(move)
            # for row in warehouse:
            #     print("".join(row))

        score = 0
        for ri, row in enumerate(warehouse):
            for ci, value in enumerate(row):
                if value == "O":
                    score += 100 * ri + ci

        return score

    def _load_warehouse_and_robot(self):
        warehouse = []
        warehouse_values = {".", "#", "@", "O"}
        robot_pos = None
        moves = []
        for ri, row in enumerate(self.input_data):
            w_row = []
            for ci, value in enumerate(row):
                if value in warehouse_values:
                    if value == "@":
                        robot_pos = (ri, ci)
                    w_row.append(value)
                elif value:
                    moves.append(value)
            if w_row:
                warehouse.append(w_row)

        return warehouse, robot_pos, moves

    def part2(self):
        return None
