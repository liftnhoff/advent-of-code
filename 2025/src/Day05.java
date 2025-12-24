import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;


public class Day05 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("2025/inputs/day05.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(List<String> lines) {
        List<List<Long>> ranges = new ArrayList<>();
        List<Long> ingredients = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("-");
            if (parts.length == 2) {
                ranges.add(new ArrayList<>());
                ranges.getLast().add(Long.parseLong(parts[0]));
                ranges.getLast().add(Long.parseLong(parts[1]));
            } else {
                if (!parts[0].isEmpty()) {
                    ingredients.add(Long.parseLong(parts[0]));
                }
            }
        }

        long freshCount = 0;
        for (long ingredient: ingredients) {
            for (List<Long> range: ranges) {
                if (ingredient >= range.get(0) && ingredient <= range.get(1)) {
                    freshCount += 1;
                    break;
                }
            }
        }

        return freshCount;
    }

    static long part2(List<String> lines) {
        List<List<Long>> ranges = new ArrayList<>();

        for (String line : lines) {
            String[] parts = line.split("-");
            if (parts.length == 2) {
                ranges.add(new ArrayList<>());
                ranges.getLast().add(Long.parseLong(parts[0]));
                ranges.getLast().add(Long.parseLong(parts[1]));
            }
        }

        ranges.sort(Comparator.comparing(List::getFirst));
        int index = 0;
        while (index < ranges.size() - 1) {
            List<Long> curRange = ranges.get(index);
            List<Long> nextRange = ranges.get(index + 1);

            if (nextRange.get(0) <= curRange.get(1)) {
                Long biggest = curRange.get(1) > nextRange.get(1) ? curRange.get(1) : nextRange.get(1);
                curRange.set(1, biggest);
                ranges.remove(index + 1);
            } else {
                index += 1;
            }
        }

        long count = 0;
        for (List<Long> range: ranges) {
            count += range.get(1) - range.get(0) + 1;
        }

        return count;
    }
}