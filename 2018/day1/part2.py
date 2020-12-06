
def load_frequency_changes(frequency_data_file):
    frequency_changes = []
    with open(frequency_data_file) as fid:
        for line in fid:
            frequency_changes.append(int(line.strip()))

    return frequency_changes


def find_first_frequency_recurrence(frequency_data_file):
    frequency = 0
    frequency_changes = load_frequency_changes(frequency_data_file)
    frequencies_reached = {frequency}
    while True:
        for change in frequency_changes:
            frequency += change
            if frequency in frequencies_reached:
                return frequency
            frequencies_reached.add(frequency)


print(find_first_frequency_recurrence('data.txt'))




