#!/bin/bash
set -euo pipefail

# Run check file format and linting.
for filename in $(git status | grep -E '(modified:)|(new file:)' | grep '.py' | sed 's/.*: *//')
do
    echo "Running isort on ${filename}"
    isort --quiet --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 "${filename}"

    echo "Running black on ${filename}"
    black "${filename}"

    echo "Running flake8 on ${filename}"
    flake8 "${filename}"
    if [ $? != 0 ]; then
        echo "ERROR  flake8 did not pass, stopping commit."
        exit 1
    fi
done

