import argparse
import importlib
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--day_number',
        help="The day number of the solution that should be run.",
        required=True,
        type=int,
    )
    args = parser.parse_args()

    # Do some slightly exotic dynamic importing depending on the day whose solution we
    # want to run.
    try:
        solution_module = importlib.import_module(f"day{args.day_number}.solution")
    except ModuleNotFoundError:
        print(f"No solution was found for day {args.day_number}.")
        sys.exit(1)

    input_file = os.path.join(f"day{args.day_number}", "input.txt")
    solution = solution_module.Solution(input_file)
    solution.run()
    print(solution.input_data)


if __name__ == "__main__":
    main()
