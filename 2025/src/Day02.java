import java.nio.file.Files;
import java.nio.file.Paths;


public class Day02 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("inputs/day02.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(java.util.List<String> lines) {
        long invalidIdSum = 0;
        for (String range : lines.getFirst().split(",")) {
            String[] parts = range.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);

            for (long value = start; value <= end; value++) {
                String valueStr = Long.toString(value);

                if (valueStr.length() % 2 == 0) {
                    String firstHalf = valueStr.substring(0, valueStr.length() / 2);
                    String secondHalf = valueStr.substring(valueStr.length() / 2);
                    if (firstHalf.equals(secondHalf)) {
                        invalidIdSum += value;
                    }
                }
            }
        }
        return invalidIdSum;
    }

    static long part2(java.util.List<String> lines) {
        long invalidIdSum = 0;
        for (String range : lines.getFirst().split(",")) {
            String[] parts = range.split("-");
            long start = Long.parseLong(parts[0]);
            long end = Long.parseLong(parts[1]);

            for (long value = start; value <= end; value++) {
                String valueStr = Long.toString(value);
                for (int index = 1; index <= valueStr.length() / 2; index++) {
                    String pattern = valueStr.substring(0, index);
                    if (isRepeatingPattern(valueStr, pattern)) {
                        invalidIdSum += value;
                        break;
                    }
                }
            }
        }
        return invalidIdSum;
    }

    static boolean isRepeatingPattern(String toCheck, String pattern) {
        String[] parts = toCheck.split(pattern);
        boolean isRP = true;
        for (String part : parts) {
            if (!part.isEmpty()) {
                isRP = false;
                break;
            }
        }
        return isRP;
    }
}