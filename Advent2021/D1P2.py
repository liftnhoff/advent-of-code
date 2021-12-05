file1 = open('D1P1_input.txt', 'r')
Lines = file1.readlines()
check = 0
count = 0
i = 0
series = len(Lines) - 2
while i < series:
    value1 = int(Lines[i])
    value2 = int(Lines[i + 1])
    value3 = int(Lines[i + 2])
    sumValues = value1 + value2 + value3
    if check != 0:
        if check < sumValues:
            count = count + 1
    check = sumValues
    i = i + 1
print(count)