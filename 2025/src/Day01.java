import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Pattern;
import java.util.regex.Matcher;


public class Day01 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("inputs/day01.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(java.util.List<String> lines) {
        int currentPos = 50;
        int dialSize = 99;
        long zeroCount = 0;

        Pattern pattern = Pattern.compile("([RL])(\\d+)");
        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                String direction = matcher.group(1);
                int count = Integer.parseInt(matcher.group(2));

                if (direction.equals("R")) {
                    currentPos += count;
                    while (currentPos > dialSize) {
                        currentPos -= dialSize + 1;
                    }
                } else if (direction.equals("L")) {
                    currentPos -= count;
                    while (currentPos < 0) {
                        currentPos += dialSize + 1;
                    }
                }

                if (currentPos == 0) {
                    zeroCount += 1;
                }

            } else {
                System.out.println("Did not match line" + line);
            }
        }
        return zeroCount;
    }

    static long part2(java.util.List<String> lines) {
        int currentPos = 50;
        int dialSize = 99;
        long zeroCount = 0;

        Pattern pattern = Pattern.compile("([RL])(\\d+)");
        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                String direction = matcher.group(1);
                int count = Integer.parseInt(matcher.group(2));

                if (direction.equals("R")) {
                    for (int tick = 0; tick < count; tick++) {
                        currentPos += 1;
                        while (currentPos > dialSize) {
                            currentPos -= dialSize + 1;
                        }
                        if (currentPos == 0) {
                            zeroCount += 1;
                        }
                    }
                } else if (direction.equals("L")) {
                    for (int tick = 0; tick < count; tick++) {
                        currentPos -= 1;
                        while (currentPos < 0) {
                            currentPos += dialSize + 1;
                        }
                        if (currentPos == 0) {
                            zeroCount += 1;
                        }
                    }
                }

            } else {
                System.out.println("Did not match line" + line);
            }
        }
        return zeroCount;
    }
}