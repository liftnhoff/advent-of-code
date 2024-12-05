from collections import defaultdict

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        before_rules_by_pn, after_rules_by_pn, updates = self.get_rules_and_updates()
        valid_updates = []
        for update in updates:
            is_valid = True
            pn_seen = set()
            for pn in update:
                if pn_seen.intersection(before_rules_by_pn[pn]):
                    is_valid = False
                    break
                pn_seen.add(pn)

            if is_valid:
                valid_updates.append(update)

        score = 0
        for update in valid_updates:
            score += update[int(len(update) / 2)]

        return score

    def part2(self):
        return None

    def get_rules_and_updates(self):
        before_rules_by_pn = defaultdict(set)
        after_rules_by_pn = defaultdict(set)
        updates = []
        for line in self.input_data:
            if "|" in line:
                rule = tuple(int(v) for v in line.split("|"))
                before_rules_by_pn[rule[0]].add(rule[1])
                after_rules_by_pn[rule[1]].add(rule[0])
            elif "," in line:
                updates.append(tuple(int(v) for v in line.split(",")))

        return before_rules_by_pn, after_rules_by_pn, updates
