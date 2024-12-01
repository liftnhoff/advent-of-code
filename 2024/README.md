# Setup

```
pyenv install 3.11.4
pyenv virtualenv 3.11.4 aoc2023
pyenv local aoc2023
pip install -r requirements.txt
```

# Run It

```
python advent_of_code.py -d 1
```

Use the test input file:

```
python advent_of_code.py -d 1 -t
```

# New Day Setup

You can create the base directory and file structure for a new day's challenge with the
`new_day.py` script:

```
python new_day.py -d 7
```

# Code Formatting

`format_files.sh` runs `isort`, `black`, and `flake8` on any modified files. Simply run
it before committing changes to autoformat the code. A git pre-commit hook can
optionally be copied to .git/hooks in the parent directory to enforce this formatting
before committing changes.
