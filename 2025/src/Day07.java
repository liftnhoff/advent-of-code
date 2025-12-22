import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;


public class Day07 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("inputs/day07.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(List<String> lines) {
        List<List<Character>> beamMap = lines.stream()
                .map(str -> str.chars()
                        .mapToObj(c -> (char) c)
                        .collect(Collectors.toList()))
                .toList();

        long splitCount = 0;

        for (int rowIndex = 0; rowIndex < beamMap.size() - 1; rowIndex++) {
            for (int colIndex = 0; colIndex < beamMap.getFirst()
                    .size(); colIndex++) {
                char value = beamMap.get(rowIndex)
                        .get(colIndex);
                if (value == '|' || value == 'S') {
                    List<Character> nextRow = beamMap.get(rowIndex + 1);
                    char nextValue = nextRow.get(colIndex);
                    if (nextValue == '^') {
                        splitCount += 1;
                        nextRow.set(colIndex - 1, '|');
                        nextRow.set(colIndex + 1, '|');
                    } else {
                        beamMap.get(rowIndex + 1)
                                .set(colIndex, '|');
                    }
                }
            }
        }

        return splitCount;
    }

    static long part2(List<String> lines) {
        return 0;
    }
}