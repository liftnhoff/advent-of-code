file = open('D2_input.txt', 'r')
lines = file.readlines()
choice = input("Choose Program (1 for position, 2 for aim): ")


def main():
    if choice == '1':
        position(lines)
    if choice == '2':
        aim(lines)


def position(lines):
    x = 0
    y = 0
    for line in lines:
        move = line.split()
        adjustment = int(move[1][0])
        if move[0] == 'forward':
            x = x + adjustment
        elif move[0] == 'down':
            y = y + adjustment
        elif move[0] == 'up':
            y = y - adjustment
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'product = {x * y}')


def aim(lines):
    x = 0
    aim = 0
    y = 0
    for line in lines:
        move = line.split()
        adjustment = int(move[1][0])
        if move[0] == 'forward':
            x = x + adjustment
            y = y + (aim * adjustment)
        elif move[0] == 'down':
            aim = aim + adjustment
        elif move[0] == 'up':
            aim = aim - adjustment
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'aim = {aim}')
    print(f'product = {x * y}')


main()
