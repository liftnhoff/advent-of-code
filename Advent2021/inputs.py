import requests
def input_files():
    day = input('Day: ')
    input_file = requests.get(f'https://adventofcode.com/2021/day/{day}/input')
    input_file.encoding = 'utf-8'
    use_file = input_file.text
    record_path = rf'file://C:/Users/morri/Documents/PyProj/Advent2021/D{day}_input.txt'
    with open(record_path, 'w') as record:
        record.write(use_file)
    file1 = open(f'D{day}_input.txt', 'r')
    Lines = file1.readlines()
    print(Lines)
input_files()
