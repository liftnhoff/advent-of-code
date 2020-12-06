
def find_boxes(data_file):
    box_ids = read_box_ids(data_file)

    for first_id in box_ids:
        for second_id in box_ids:
            common_letters = find_common_letters(first_id, second_id)
            if common_letters:
                return common_letters

    raise RuntimeError('Could not find corresponding boxes.')


def find_common_letters(first_id, second_id):
    if len(first_id) != len(second_id):
        raise RuntimeError('ID strings must be the same length.')

    common_letters = []
    diff_count = 0
    for index in range(len(first_id)):
        if first_id[index] == second_id[index]:
            common_letters.append(first_id[index])
        else:
            diff_count += 1

        if diff_count >= 2:
            return ''

    if diff_count == 0:
        return ''
    else:
        return ''.join(common_letters)


def read_box_ids(data_file):
    with open(data_file) as fid:
        box_ids = fid.read().strip().split('\n')
    return box_ids


print(find_boxes('data.txt'))
