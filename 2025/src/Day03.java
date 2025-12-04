import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.stream.Collectors;


public class Day03 {
    public static void main(String[] args) throws Exception {
        var lines = Files.readAllLines(Paths.get("inputs/day03.txt"));
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }

    static long part1(java.util.List<String> lines) {
        int maxVoltage = 0;
        for (String line : lines) {
            maxVoltage += determineMaxVoltage(line);
        }
        return maxVoltage;
    }

    static int determineMaxVoltage(String batteryBank) {
        int[] voltages = batteryBank.chars().map(c -> c - '0').toArray();
        int leftMax = 0;
        int rightMax = 0;
        for (int index = 0; index < voltages.length - 1; index++) {
            int voltage = voltages[index];
            if (voltage > leftMax) {
                leftMax = voltage;
                rightMax = 0;
                continue;
            }
            if (voltage > rightMax) {
                rightMax = voltage;
            }
        }
        int voltage = voltages[voltages.length - 1];
        if (voltage > rightMax) {
            rightMax = voltage;
        }

        return 10 * leftMax + rightMax;
    }

    static long part2(java.util.List<String> lines) {
        long maxVoltage = 0;
        for (String line : lines) {
            maxVoltage += determineMaxVoltagePart2(line);
        }
        return maxVoltage;
    }

    static long determineMaxVoltagePart2(String batteryBank) {
        int[] voltages = batteryBank.chars().map(c -> c - '0').toArray();
        int[] highVoltages = new int[12];

        int earliestIndex = 0;
        for (int eo = highVoltages.length; eo > 0; eo--) {
            int latestIndex = voltages.length - eo + 1;
            int[] batterySubBank = Arrays.copyOfRange(voltages, earliestIndex, latestIndex);

            Voltage ebv = findEarliestBiggestVoltage(batterySubBank);
            earliestIndex += ebv.index() + 1;
            highVoltages[highVoltages.length - eo] = ebv.value();
        }

        String voltageStr = Arrays.stream(highVoltages).mapToObj(String::valueOf).collect(Collectors.joining());
        return Long.parseLong(voltageStr);
    }

    static Voltage findEarliestBiggestVoltage(int[] voltages) {
        int biggestVoltage = 0;
        int index = voltages.length - 1;
        for (int vi = voltages.length - 1; vi >= 0; vi--) {
            if (voltages[vi] >= biggestVoltage) {
                biggestVoltage = voltages[vi];
                index = vi;
            }
        }

        return new Voltage(biggestVoltage, index);
    }
}


record Voltage(int value, int index) {
}

