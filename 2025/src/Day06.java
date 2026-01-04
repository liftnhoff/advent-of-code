import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;


public class Day06 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("2025/inputs/day06.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(List<String> lines) {
        List<List<Long>> numbers = new ArrayList<>();
        for (int index = 0; index < lines.size() - 1; index++) {
            numbers.add(Arrays.stream(lines.get(index).strip().split(" +"))
                                .filter(s -> s.matches("-?\\d+"))
                                .map(Long::parseLong)
                                .collect(Collectors.toList()));
        }

        List<String> operators = List.of(lines.getLast().strip().split(" +"));

        long total = 0L;
        for (int colIndex = 0; colIndex < operators.size(); colIndex++) {
            long answer = 0L;
            if (operators.get(colIndex).equals("+")) {
                for (List<Long> row : numbers) {
                    answer += row.get(colIndex);
                }
            } else {
                answer = 1L;
                for (List<Long> row : numbers) {
                    answer *= row.get(colIndex);
                }
            }
            total += answer;
        }

        return total;
    }

    static long part2(List<String> lines) {
        List<Integer> numbers = new ArrayList<Integer>();

        long total = 0L;
        for (int ci = lines.getFirst().length() - 1; ci >= 0; ci--) {
            long answer = 0L;
            StringBuilder numberBuilder = new StringBuilder();
            for (int ri = 0; ri < lines.size(); ri++) {
                char value = lines.get(ri).charAt(ci);
                if (value == '+') {
                    numbers.add(Integer.parseInt(numberBuilder.toString()));
                    answer = 0L;
                    for (int nn : numbers) {
                        answer += nn;
                    }
                } else if (value == '*') {
                    numbers.add(Integer.parseInt(numberBuilder.toString()));
                    answer = 1L;
                    for (int nn : numbers) {
                        answer *= nn;
                    }
                } else if (value != ' ') {
                    numberBuilder.append(value);
                }
            }
            if (answer == 0) {
                String numberString = numberBuilder.toString();
                if (!numberString.isEmpty()) {
                    numbers.add(Integer.parseInt(numberString));
                }
            } else {
                total += answer;
                numbers = new ArrayList<Integer>();
            }
        }
        return total;
    }
}