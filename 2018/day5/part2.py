from part1 import read_polymer_file, PolymerReactor


def main():
    polymer = read_polymer_file('data.txt')

    polymer_reactor = PolymerReactor()
    units_to_remove = sorted(set(polymer.lower()))
    min_reacted_length = len(polymer)
    for lower_unit in units_to_remove:
        upper_unit = lower_unit.upper()
        reduced_polymer = [
            unit for unit in polymer if unit != lower_unit and unit != upper_unit
        ]
        reacted_polymer = polymer_reactor.react(reduced_polymer)
        reacted_length = len(reacted_polymer)
        print(f'{lower_unit}  {reacted_length}')

        if reacted_length < min_reacted_length:
            min_reacted_length = reacted_length

    print(min_reacted_length)


if __name__ == '__main__':
    main()
