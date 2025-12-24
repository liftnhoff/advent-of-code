import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Day04 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("2025/inputs/day04.txt"));

        List<List<Character>> charGrid = lines.stream()
                .map(str -> str.chars()
                        .mapToObj(c -> (char) c)
                        .collect(Collectors.toList()))
                .toList();

        System.out.println("Part 1: " + part1(charGrid));
        System.out.println("Part 2: " + part2(charGrid));
    }

    static long part1(List<List<Character>> charGrid) {
        int rowCount = charGrid.size();
        int colCount = charGrid.getFirst().size();

        long moveableCount = 0;
        for (int rowIndex = 0; rowIndex < rowCount; rowIndex++) {
            for (int colIndex = 0; colIndex < colCount; colIndex++) {
                if (charGrid.get(rowIndex).get(colIndex) == '.') {
                    continue;
                }

                int freeSpaces = 0;
                for (int ro = -1; ro < 2; ro++) {
                    for (int co = -1; co < 2; co++) {
                        int ri = rowIndex + ro;
                        int ci = colIndex + co;
//                        System.out.printf("%3d %3d %3d\n", ri, ci, freeSpaces);
                        if (ro == 0 && co == 0) {
                            continue;
                        }
                        if (ri < 0 || ri >= rowCount) {
                            freeSpaces += 1;
                            continue;
                        }
                        if (ci < 0 || ci >= colCount) {
                            freeSpaces += 1;
                            continue;
                        }

                        if (charGrid.get(ri).get(ci) == '.') {
                            freeSpaces += 1;
                        }
                    }
                }

                if (freeSpaces >= 5) {
                    moveableCount += 1;
                }
            }
        }

        return moveableCount;
    }

    static long part2(List<List<Character>> charGrid) {
        return 0;
    }
}
