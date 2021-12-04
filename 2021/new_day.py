import argparse
import os
import sys


def main():
    args = _parse_arguments()
    _make_solution_directory(args.day_number)


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--day_number",
        help="The day number of the solution that should be run.",
        required=True,
        type=int,
    )
    return parser.parse_args()


def _make_solution_directory(day_number: int) -> None:
    aoc_dir = os.path.dirname(os.path.realpath(__file__))
    day_dir = os.path.join(aoc_dir, f"day{day_number}")

    try:
        os.mkdir(day_dir)
    except FileExistsError:
        print(f"There is already a solution directory for day {day_number}.")
        sys.exit(1)

    open(os.path.join(day_dir, "__init__.py"), "a").close()
    open(os.path.join(day_dir, "test_input.txt"), "a").close()
    open(os.path.join(day_dir, "input.txt"), "a").close()

    solution_file = os.path.join(day_dir, "solution.py")
    if not os.path.isfile(solution_file):
        with open(solution_file, "w") as fid:
            fid.write(_SOLUTION_TEMPLATE)

    print(f"Created solution directory {day_dir}")


_SOLUTION_TEMPLATE = """\
from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        return None

    def part2(self):
        return None
"""


if __name__ == "__main__":
    main()
