import { readFileSync } from "fs";

function main() {
  let lines = loadInput("input.txt");
  console.log("Part 1: " + part1(lines));
  console.log("Part 2: " + part2(lines));
}

function loadInput(filepath: string): string[] {
  return readFileSync(filepath, "utf-8").split("\n");
}

function part1(lines: string[]): number {
  return 0;
}

function part2(lines: string[]): number {
  return 0;
}

main();
