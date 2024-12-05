from collections import defaultdict

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        before_rules_by_pn, updates = self.get_rules_and_updates()
        valid_updates = []
        for update in updates:
            if self.is_order_valid(before_rules_by_pn, update):
                valid_updates.append(update)

        score = 0
        for update in valid_updates:
            score += update[int(len(update) / 2)]

        return score

    def part2(self):
        before_rules_by_pn, updates = self.get_rules_and_updates()
        invalid_updates = []
        for update in updates:
            if not self.is_order_valid(before_rules_by_pn, update):
                invalid_updates.append(update)

        fixed_updates = []
        for update in invalid_updates:
            new_update = []
            for pn in update:
                new_update.append(pn)
                if not self.is_order_valid(before_rules_by_pn, new_update):
                    new_update.pop()
                    for index in range(len(new_update)):
                        new_update.insert(index, pn)
                        if self.is_order_valid(before_rules_by_pn, new_update):
                            break
                        else:
                            new_update.pop(index)
            fixed_updates.append(new_update)

        score = 0
        for update in fixed_updates:
            score += update[int(len(update) / 2)]

        return score

    def get_rules_and_updates(self):
        before_rules_by_pn = defaultdict(set)
        updates = []
        for line in self.input_data:
            if "|" in line:
                rule = tuple(int(v) for v in line.split("|"))
                before_rules_by_pn[rule[0]].add(rule[1])
            elif "," in line:
                updates.append(tuple(int(v) for v in line.split(",")))

        return before_rules_by_pn, updates

    def is_order_valid(self, before_rules_by_pn, update):
        is_valid = True
        pn_seen = set()
        for pn in update:
            if pn_seen.intersection(before_rules_by_pn[pn]):
                is_valid = False
                break
            pn_seen.add(pn)

        return is_valid
