import argparse
import os


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

    os.mkdir(day_dir)

    open(os.path.join(day_dir, "__init__.py"), 'a').close()
    open(os.path.join(day_dir, "solution.py"), 'a').close()
    open(os.path.join(day_dir, "test_input.txt"), 'a').close()
    open(os.path.join(day_dir, "input.txt"), 'a').close()

    print(f"Created solution directory {day_dir}")


if __name__ == "__main__":
    main()
