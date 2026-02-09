import { readFileSync } from "fs";

function main() {
    let lines = loadInput("input.txt");
    // let lines = loadInput("test-input.txt");
    console.log("Part 1: " + part1(lines));
    console.log("Part 2: " + part2(lines));
}

function loadInput(filepath: string): string[] {
    return readFileSync(filepath, "utf-8").split("\n");
}

function part1(lines: string[]): number {
    const dialMax: number = 99;
    let position: number = 50;
    let zeroCount: number = 0;

    for (const line of lines) {
        if (line.length == 0) {
            continue;
        }

        let direction = line[0];
        let amount: number = Number(line.substring(1));
        if (direction == "R") {
            position += amount;
            while (position > dialMax) {
                position -= dialMax + 1;
            }
        } else {
            position -= amount;
            while (position < 0) {
                position += dialMax + 1;
            }
        }

        if (position == 0) {
            zeroCount += 1;
        }
    }

    return zeroCount;
}

function part2(lines: string[]): number {
    const dialMax: number = 99;
    let position: number = 50;
    let zeroCount: number = 0;

    for (const line of lines) {
        if (line.length == 0) {
            continue;
        }

        let direction = line[0];
        let amount: number = Number(line.substring(1));
        if (direction == "R") {
            for (let index = 0; index < amount; index++) {
                position += 1;
                if (position > dialMax) {
                    position -= dialMax + 1;
                }
                if (position == 0) {
                    zeroCount += 1;
                }
            }
        } else {
            for (let index = 0; index < amount; index++) {
                position -= 1;
                if (position < 0) {
                    position += dialMax + 1;
                }
                if (position == 0) {
                    zeroCount += 1;
                }
            }
        }
    }

    return zeroCount;
}

main();
