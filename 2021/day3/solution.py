from collections import Counter, defaultdict
from dataclasses import dataclass

from base.solution import AdventOfCodeSolutionBase


@dataclass
class BinnedBits:
    zero_count: int
    one_count: int
    values_with_zero_in_index: list[str]
    values_with_one_in_index: list[str]


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
        return self._get_oxygen_generator_rating() * self._get_co2_scrubber_rating()

    def _get_oxygen_generator_rating(self) -> int:
        current_values = self.input_data[:]
        for index in range(len(self.input_data[0])):
            binned_bits = self._bin_bits(current_values, index)
            if binned_bits.zero_count > binned_bits.one_count:
                current_values = binned_bits.values_with_zero_in_index
            else:
                current_values = binned_bits.values_with_one_in_index

            if len(current_values) <= 1:
                break

        return int(current_values[0], 2)

    def _bin_bits(self, bits_list: list[str], index: int) -> BinnedBits:
        binned_bits = BinnedBits(0, 0, [], [])
        for value in bits_list:
            if value[index] == "0":
                binned_bits.zero_count += 1
                binned_bits.values_with_zero_in_index.append(value)
            else:
                binned_bits.one_count += 1
                binned_bits.values_with_one_in_index.append(value)

        return binned_bits

    def _get_co2_scrubber_rating(self) -> int:
        current_values = self.input_data[:]
        for index in range(len(self.input_data[0])):
            binned_bits = self._bin_bits(current_values, index)
            if binned_bits.zero_count <= binned_bits.one_count:
                current_values = binned_bits.values_with_zero_in_index
            else:
                current_values = binned_bits.values_with_one_in_index

            if len(current_values) <= 1:
                break

        return int(current_values[0], 2)
