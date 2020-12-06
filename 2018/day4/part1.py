from collections import defaultdict
import datetime
import re


def main():
    guard_times = read_guard_times('data.txt')

    sleep_times_by_guard_id, sleep_totals_by_guard_id = record_sleep_times(guard_times)
    # pretty_print_sleep_times(sleep_times_by_guard_id)
    # print(sleep_totals_by_guard_id)

    sleepiest_guard_id = find_sleepiest_guard(sleep_totals_by_guard_id)
    most_slept_minute = find_most_slept_minute(sleep_times_by_guard_id[sleepiest_guard_id])

    print(
        f'Guard {sleepiest_guard_id} is the sleepiest and sleeps the most at minute'
        f' {most_slept_minute}. Answer: {sleepiest_guard_id * most_slept_minute}'
    )



def read_guard_times(data_file):
    components_regex = re.compile(r'^\[(.+)\] (.+)$')
    records = []
    with open(data_file) as fid:
        for line in fid:
            match = components_regex.match(line)
            record_time = datetime.datetime.strptime(match.group(1), '%Y-%m-%d %H:%M')
            records.append((record_time, match.group(2)))

    return sorted(records, key=lambda x: x[0])


def record_sleep_times(guard_times):
    guard_start_regex = re.compile(r'Guard #(\d+) begins shift')
    sleep_times_by_guard_id = defaultdict(list)
    sleep_totals_by_guard_id = defaultdict(int)
    guard_id = None
    asleep_minute = None
    for record_time, detail in guard_times:
        match = guard_start_regex.match(detail)
        if match:
            guard_id = int(match.group(1))
            sleep_times_by_guard_id[guard_id].append([0] * 60)
            continue

        if detail == 'falls asleep':
            asleep_minute = record_time.minute

        if detail == 'wakes up':
            wake_minute = record_time.minute
            for index in range(asleep_minute, wake_minute):
                sleep_times_by_guard_id[guard_id][-1][index] = 1
            sleep_totals_by_guard_id[guard_id] += wake_minute - asleep_minute
            asleep_minute = None

    return sleep_times_by_guard_id, sleep_totals_by_guard_id


def pretty_print_sleep_times(sleep_times_by_guard_id):
    for guard_id, sleep_times in sleep_times_by_guard_id.items():
        print(guard_id)
        for row in sleep_times:
            print(row)


def find_sleepiest_guard(sleep_totals_by_guard_id):
    max_sleep = 0
    max_sleep_guard_id = None
    for guard_id, sleep_total in sleep_totals_by_guard_id.items():
        if sleep_total > max_sleep:
            max_sleep = sleep_total
            max_sleep_guard_id = guard_id
    return max_sleep_guard_id


def find_most_slept_minute(sleep_times):
    minute_sleep_count = [0] * 60
    for record in sleep_times:
        for index, value in enumerate(record):
            minute_sleep_count[index] += value

    most_slept_minute = max(
        range(len(minute_sleep_count)),
        key=minute_sleep_count.__getitem__
    )
    return most_slept_minute


if __name__ == '__main__':
    main()
