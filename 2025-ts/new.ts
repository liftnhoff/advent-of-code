import { copyFileSync, mkdirSync, writeFileSync } from "fs";
import { parseArgs } from "util";

function main() {
  const { values, positionals } = parseArgs({
    options: {
      day: { type: "string", short: "d" },
    },
  });

  let day: string = values.day;
  if (day == null) {
    console.warn("\nPlease specify a day number with -d.");
    return;
  }

  let dirPath = "day" + day;
  mkdirSync(dirPath);

  copyFileSync("base/base.ts", dirPath + "/main.ts");

  writeFileSync(dirPath + "/input.txt", "");
  writeFileSync(dirPath + "/test-input.txt", "");
}

main();
