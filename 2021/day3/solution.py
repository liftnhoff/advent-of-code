from collections import Counter, defaultdict

from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        bit_counter_by_index = defaultdict(Counter)
        for bit_row in self.input_data:
            for index, bit in enumerate(bit_row):
                bit_counter_by_index[index].update(bit)

        gamma_rate_bits = "".join(
            counter.most_common(1)[0][0] for counter in bit_counter_by_index.values()
        )
        epsilon_rate_bits = "".join(
            "1" if bit == "0" else "0" for bit in gamma_rate_bits
        )
        gamma_rate_value = int(gamma_rate_bits, 2)
        epsilon_rate_value = int(epsilon_rate_bits, 2)

        return gamma_rate_value * epsilon_rate_value

    def part2(self):
        return
