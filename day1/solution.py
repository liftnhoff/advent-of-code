from typing import List


def main():
    data = read_data()

    fuel_values = [fuel_for_mass(module_mass) for module_mass in data]
    print(f'PART 1 ANSWER: {sum(fuel_values)}')

    fuel_values = [determine_total_fuel_required(module_mass) for module_mass in data]
    print(f'PART 2 ANSWER: {sum(fuel_values)}')


def read_data() -> List[int]:
    with open('data.txt') as fid:
        data = [int(line.strip()) for line in fid]
    return data


def fuel_for_mass(mass: int) -> int:
    return (mass // 3) - 2


def determine_total_fuel_required(mass: int) -> int:
    fuel = fuel_for_mass(mass)
    if fuel < 0:
        fuel = 0
    else:
        fuel += determine_total_fuel_required(fuel)
    return fuel


if __name__ == '__main__':
    main()
