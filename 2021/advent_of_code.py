import argparse
import importlib
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


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


    solution_module = importlib.import_module(f"day{args.day_number}.solution")
    s = solution_module.Solution()
    s.run()


if __name__ == "__main__":
    main()
