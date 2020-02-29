

function main() {
    // console.log(isValidCombination(111111));
    // console.log(isValidCombination(223450));
    // console.log(isValidCombination(123789));
    console.log(combinationCount());

    // console.log(isValidCombinationNoGroups(111111));
    // console.log(isValidCombinationNoGroups(112233));
    // console.log(isValidCombinationNoGroups(123444));
    // console.log(isValidCombinationNoGroups(111122));
    console.log(combinationCountNoGroups());
}


function combinationCount() {
    let min = 240920;
    let max = 789857;

    let count = 0;
    for (let combination = min; combination <= max; combination++) {
        count += isValidCombination(combination);
    }

    return count;
}


function isValidCombination(value) {
    let valueStr = value.toString();
    let previousDigit = -1;
    let isIncreasing = true;
    let hasDouble = false;
    for (let char of valueStr) {
        let digit = parseInt(char);
        if (digit == previousDigit) {
            hasDouble = true;
        }
        else if (digit < previousDigit) {
            isIncreasing = false;
            break;
        }
        previousDigit = digit;
    }

    return isIncreasing && hasDouble;
}


function combinationCountNoGroups() {
    let min = 240920;
    let max = 789857;

    let count = 0;
    for (let combination = min; combination <= max; combination++) {
        count += isValidCombinationNoGroups(combination);
    }

    return count;
}


function isValidCombinationNoGroups(value) {
    let valueStr = value.toString();
    let previousDigit = -1;
    let isIncreasing = true;
    let hasDouble = false;
    let currentGroupCount = 1;
    for (let char of valueStr) {
        let digit = parseInt(char);
        if (digit == previousDigit) {
            currentGroupCount++;
        }
        else {
            if (currentGroupCount == 2) {
                hasDouble = true;
            }
            currentGroupCount = 1;
        }

        if (digit < previousDigit) {
            isIncreasing = false;
            break;
        }
        previousDigit = digit;
    }

    if (currentGroupCount == 2) {
        hasDouble = true;
    }

    return isIncreasing && hasDouble;
}


main();
