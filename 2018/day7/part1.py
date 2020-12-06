from instructions import Instructions


def main():
    instructions = Instructions.read_instructions('data/data.txt')
    print(instructions.determine_step_order())


if __name__ == '__main__':
    main()
