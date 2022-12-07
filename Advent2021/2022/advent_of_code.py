import argparse
import importlib
import os
import sys


def main():
    args = _parse_arguments()
    _run_solution_for_day(args.day_number, args.test)


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--day_number",
        help="The day number of the solution that should be run.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-t",
        "--test",
        help="If test input should be used instead of true input data.",
        action="store_true",
    )
    return parser.parse_args()


def _run_solution_for_day(day_number: int, is_test: bool) -> None:
    # Do some slightly exotic dynamic importing depending on the day to run.
    try:
        solution_module = importlib.import_module(f"day{day_number}.solution")
    except ModuleNotFoundError:
        print(f"No solution was found for day {day_number}.")
        sys.exit(1)

    aoc_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_name = "test_input.txt" if is_test else "input.txt"
    input_file_path = os.path.join(aoc_dir, f"day{day_number}", input_file_name)

    solution = solution_module.Solution(input_file_path)
    solution.run()


if __name__ == '__main__':
    main()
