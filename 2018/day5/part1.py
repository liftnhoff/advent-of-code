def main():
    # polymer = 'dabAcCaCBAcCcaDA'
    # polymer = 'zabcdefghijJIHGFEDCBA'
    # polymer = 'abAcCaCBAcCcaA'
    # print(polymer)
    polymer = read_polymer_file('data.txt')

    polymer_reactor = PolymerReactor()
    new_polymer = polymer_reactor.react(polymer)
    print(new_polymer)
    print(len(new_polymer))


def read_polymer_file(data_file):
    with open(data_file) as fid:
        polymer = fid.read().strip()
    return polymer


class PolymerReactor:
    NULL_UNIT = '-'

    def __init__(self):
        self._polymer = None
        self._current_index = None
        self._max_current_index = None
        self._next_index = None
        self._max_next_index = None

    def react(self, polymer_string):
        self._initialize_reaction(polymer_string)
        while self._current_index <= self._max_current_index:
            self._process_reaction()

        new_polymer = [unit for unit in self._polymer if unit != self.NULL_UNIT]
        return ''.join(new_polymer)

    def _initialize_reaction(self, polymer_string):
        self._polymer = list(polymer_string)
        self._current_index = 0
        self._max_current_index = len(self._polymer) - 2
        self._next_index = 0
        self._max_next_index = self._max_current_index + 1
        self._previous_non_reacted_index = 0

    def _process_reaction(self):
        current_unit = self._get_current_unit()
        if current_unit == self.NULL_UNIT or self._current_index > self._max_current_index:
            return
        next_unit = self._get_next_unit()

        if self._units_react(current_unit, next_unit):
            self._polymer[self._current_index] = self.NULL_UNIT
            self._polymer[self._next_index] = self.NULL_UNIT
            self._reset_to_previous_non_reacted_index()
        else:
            self._current_index += 1

    def _get_current_unit(self):
        unit = self._polymer[self._current_index]
        while unit == self.NULL_UNIT and self._current_index <= self._max_current_index:
            self._current_index += 1
            unit = self._polymer[self._current_index]
        return unit

    def _get_next_unit(self):
        self._next_index = self._current_index + 1
        unit = self._polymer[self._next_index]
        while unit == self.NULL_UNIT and self._next_index < self._max_next_index:
            self._next_index += 1
            unit = self._polymer[self._next_index]
        return unit

    def _reset_to_previous_non_reacted_index(self):
        unit = self._polymer[self._current_index]
        while unit == self.NULL_UNIT and self._current_index > 0:
            self._current_index -= 1
            unit = self._polymer[self._current_index]
        return unit

    @staticmethod
    def _units_react(first, second):
        if first != second and first.lower() == second.lower():
            return True
        else:
            return False


if __name__ == '__main__':
    main()
