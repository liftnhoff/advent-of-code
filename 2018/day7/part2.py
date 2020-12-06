from instructions import Instructions


def main():
    instructions = Instructions.read_instructions('data/data.txt')

    step_duration_base = 60
    worker_count = 5
    print(instructions.determine_step_order_with_time(step_duration_base, worker_count))


if __name__ == '__main__':
    main()
