from part1 import read_guard_times, record_sleep_times, pretty_print_sleep_times


def main():
    guard_times = read_guard_times('data.txt')

    sleep_times_by_guard_id, _ = record_sleep_times(guard_times)
    # pretty_print_sleep_times(sleep_times_by_guard_id)

    most_consistent_guard_id, most_slept_minute = find_most_consistently_slept_minute(
        sleep_times_by_guard_id
    )

    print(
        f'Guard {most_consistent_guard_id} is the sleepiest and sleeps the most at minute'
        f' {most_slept_minute}. Answer: {most_consistent_guard_id * most_slept_minute}'
    )


def find_most_consistently_slept_minute(sleep_times_by_guard_id):
    """
    Returns:
        tuple: Guard that sleeps the same minute most consistently and the minute that
            the guard is most consistently asleep.
    """
    max_most_slept_count = 0
    most_slept_minute = None
    most_consistent_guard_id = None
    for guard_id, sleep_times in sleep_times_by_guard_id.items():
        minute_sleep_count = [0] * 60
        for record in sleep_times:
            for index, value in enumerate(record):
                minute_sleep_count[index] += value

        guard_most_slept_minute = max(
            range(len(minute_sleep_count)),
            key=minute_sleep_count.__getitem__
        )
        most_slept_count = minute_sleep_count[guard_most_slept_minute]

        if most_slept_count > max_most_slept_count:
            max_most_slept_count = most_slept_count
            most_slept_minute = guard_most_slept_minute
            most_consistent_guard_id = guard_id

    return most_consistent_guard_id, most_slept_minute


if __name__ == '__main__':
    main()
