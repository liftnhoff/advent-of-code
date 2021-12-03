# Setup
```
pyenv virtualenv 3.9.1 aoc2021
pyenv local aoc2021
pip install -r requirements.txt
```

# Run It
```
python advent_of_code.py -d 1
```

# Code Formatting
`format_files.sh` runs `isort`, `black`, and `flake8` on any modified files. Simply run
it before committing changes to autoformat the code. A git precommit hook is not
currently set up so you need to run it manually.
