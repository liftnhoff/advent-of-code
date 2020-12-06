

with open('data.txt') as fid:
    frequency = 0
    for line in fid:
        frequency_change = int(line.strip())
        frequency += frequency_change

print(frequency)





