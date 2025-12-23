import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
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
        long split = -9L;

        List<List<Long>> beamMap = new ArrayList<>();
        for (int rowIndex = 0; rowIndex < lines.size(); rowIndex++) {
            beamMap.add(new ArrayList<>());
            for (char value : lines.get(rowIndex)
                    .toCharArray()) {
                if (value == 'S') {
                    beamMap.get(rowIndex)
                            .add(1L);
                } else if (value == '^') {
                    beamMap.get(rowIndex)
                            .add(split);
                } else {
                    beamMap.get(rowIndex)
                            .add(0L);
                }
            }
        }

        for (int rowIndex = 0; rowIndex < beamMap.size() - 1; rowIndex++) {
            for (int colIndex = 0; colIndex < beamMap.getFirst()
                    .size(); colIndex++) {
                long value = beamMap.get(rowIndex)
                        .get(colIndex);
                if (value > 0) {
                    List<Long> nextRow = beamMap.get(rowIndex + 1);
                    long nextValue = nextRow.get(colIndex);
                    if (nextValue == split) {
                        nextRow.set(colIndex - 1, value + nextRow.get(colIndex - 1));
                        nextRow.set(colIndex + 1, value + nextRow.get(colIndex + 1));
                    } else {
                        nextRow.set(colIndex, value + nextRow.get(colIndex));
                    }
                }
            }
        }

//        for (List<Long> row : beamMap) {
//            System.out.println(row.stream()
//                    .map(n -> String.format("%3d", n))
//                    .collect(Collectors.joining()));
//        }

        return beamMap.getLast().stream().mapToLong(Long::longValue).sum();
    }

    static long part2_permutation(List<String> lines) {
        List<List<Character>> beamMap = lines.stream()
                .map(str -> str.chars()
                        .mapToObj(c -> (char) c)
                        .collect(Collectors.toList()))
                .toList();

        List<List<ParticlePos>> paths = new ArrayList<>();
        List<Character> firstRow = beamMap.getFirst();
        for (int colIndex = 0; colIndex < firstRow.size(); colIndex++) {
            if (firstRow.get(colIndex) == 'S') {
                ArrayList<ParticlePos> path = new ArrayList<>();
                path.add(new ParticlePos(0, colIndex));
                paths.add(path);
            }
        }

        long pathCount = 1;
        while (!paths.isEmpty()) {
            List<ParticlePos> currentPath = paths.removeFirst();
            while (currentPath.getLast()
                    .rowIndex() < beamMap.size() - 1) {
                ParticlePos currentPos = currentPath.getLast();
                List<Character> nextRow = beamMap.get(currentPos.rowIndex() + 1);

                if (nextRow.get(currentPos.colIndex()) == '^') {
                    pathCount += 1;

                    List<ParticlePos> altPath = new ArrayList<>();
                    altPath.add(new ParticlePos(currentPos.rowIndex() + 1, currentPos.colIndex() + 1));
                    paths.add(altPath);

                    currentPath.add(new ParticlePos(currentPos.rowIndex() + 1, currentPos.colIndex() - 1));
                } else {
                    currentPath.add(new ParticlePos(currentPos.rowIndex() + 1, currentPos.colIndex()));
                }
            }
        }

        return pathCount;
    }
}


record ParticlePos(int rowIndex, int colIndex) {
}
