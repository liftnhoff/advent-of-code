file3 = open('D3_input.txt', 'r')
lines_one = file3.readlines()
file3_2 = open('D3_input.txt', 'r')
lines_two = file3_2.readlines()


def o2(lines):
    oxygen = ''
    index = 0
    item_len = len(lines[0]) - 1
    for p in range(0, item_len):
        print(f'p= {p}')
        print(lines)
        zeros = 0
        ones = 0
        if len(lines) > 2:
            for line in lines:
                if line[p] == '0':
                    zeros += 1
                else:
                    ones += 1
            if zeros <= ones:
                oxygen = oxygen + '0'
            else:
                oxygen = oxygen + '1'
            print(f'zero = {zeros}  one = {ones}')
            dropper = oxygen[p]
            drops = []
            print(f'dropper value = {dropper}')
            lines_len = len(lines)
            print(f'{p} stage length = {lines_len}')
            for d in range(0, lines_len):
                # print(f'd= {d}')
                # print(f'line = {lines[d]}')
                if lines[d][p] == oxygen[p]:
                    drops.insert(index, d)
                    index += 1
            drops.reverse()
            print(f'dropping {p}')
            for i in drops:
                lines.pop(i)
            print(f'o2 current = {oxygen}')
        elif len(lines) <= 2:
            if lines[0][p] == '1':
                oxygen = lines[0]
            elif len(lines) == 2 and lines[1][p] == '1':
                oxygen = lines[1]
    print(f'oxygen_string= {oxygen}')
    oxygen = int(oxygen[:12], 2)
    print(f'o2 number= {oxygen}')
    return oxygen


def co2_scrubber(lines_2):
    co2 = ''
    item_len2 = len(lines_2[0]) - 1
    for p in range(0, item_len2):
        print(f'p={p}')
        print(lines_2)
        zeros = 0
        ones = 0
        if len(lines_2) > 2:
            for line in lines_2:
                if line[p] == '0':
                    zeros += 1
                else:
                    ones += 1
            if zeros > ones:
                co2 += '0'
            else:
                co2 += '1'
            print(f'zero = {zeros}  one = {ones}')
            dropper = co2[p]
            dropping = []
            index2 = 0
            print(f'dropper value = {dropper}')
            lines_2_len = len(lines_2)
            print(f'{p} stage length = {lines_2_len}')
            for d in range(0, lines_2_len):
                if lines_2[d][p] == co2[p]:
                    dropping.insert(index2, d)
                    index2 += 1
            dropping.reverse()
            print(f'dropping {p}')
            for i in dropping:
                lines_2.pop(i)
            print(f'co2 current = {co2}')
        elif len(lines_2) <= 2:
            if lines_2[0][p] == '0':
                co2 = lines_2[0]
            elif len(lines_2) == 2 and lines_2[1][p] == '0':
                co2 = lines_2[1]
    print(f'co2 Final = {co2[:12]}')
    co2 = int(co2[:11], 2)
    print(f'co2 number = {co2}')
    return co2


print(f'final = {o2(lines_one) * co2_scrubber(lines_two)}')
