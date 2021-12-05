file1 = open('D1P1_input.txt', 'r')
Lines = file1.readlines()
check = 0
count = 0
for line in Lines:
    value = int(line)
    if check != 0:
        if check < value:
            count = count + 1
    check = value
print(count)
