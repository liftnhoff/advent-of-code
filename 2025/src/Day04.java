import java.nio.file.Files;
import java.nio.file.Paths;

public class Day04 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("inputs/day03.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(java.util.List<String> lines) {
        return 0;
    }

    static long part2(java.util.List<String> lines) {
        return 0;
    }
}


class PaperMap {

    private char[][] positions = new char[][];

    void PaperMap() {

    }

    public char[][] getPositions() {
        return positions;
    }

    public void setPositions(char[][] positions) {
        this.positions = positions;
    }
}