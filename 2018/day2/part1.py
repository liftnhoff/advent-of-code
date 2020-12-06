from collections import Counter


def box_ids_checksum(data_file):
    box_ids = read_box_ids(data_file)
    two_count = 0
    three_count = 0
    for box_id in box_ids:
        counts = Counter(box_id)

        found_two_count = False
        found_three_count = False
        for count in counts.values():
            if not found_two_count and count == 2:
                two_count += 1
                found_two_count = True
            if not found_three_count and count == 3:
                three_count += 1
                found_three_count = True

    return two_count * three_count



def read_box_ids(data_file):
    with open(data_file) as fid:
        box_ids = fid.read().strip().split('\n')
    return box_ids



print(box_ids_checksum('data.txt'))
