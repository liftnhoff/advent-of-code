import re


def main():
    fabric_claims = read_fabric_claims('data.txt')
    fabric = make_fabric(fabric_claims)

    fabric = mark_fabric(fabric, fabric_claims)
    overlap_squares = count_claim_overlaps(fabric)
    print(overlap_squares)


def read_fabric_claims(data_file):
    with open(data_file) as fid:
        claim_specs = fid.read().strip().split('\n')

    return [FabricClaim.from_spec(spec) for spec in claim_specs]


class FabricClaim:
    SPEC_REGEX = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')

    @classmethod
    def from_spec(cls, spec):
        match = cls.SPEC_REGEX.match(spec)
        if match:
            return cls(
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4)),
                int(match.group(5)),
            )
        else:
            raise ValueError('Invalid FabricClaim spec.')

    def __init__(self, claim_id, start_col, start_row, col_count, row_count):
        self.claim_id = claim_id
        self.start_col = start_col
        self.start_row = start_row
        self.col_count = col_count
        self.row_count = row_count

        self.end_col = self.start_col + self.col_count
        self.end_row = self.start_row + self.row_count

    def __str__(self):
        return f'#{self.claim_id} @ {self.start_col},{self.start_row}: {self.col_count}x{self.row_count}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self}'


def make_fabric(fabric_claims):
    max_row = 0
    max_col = 0
    for claim in fabric_claims:
        if claim.end_row > max_row:
            max_row = claim.end_row

        if claim.end_col > max_col:
            max_col = claim.end_col

    fabric = []
    for row in range(max_row):
        fabric.append([0] * max_col)

    return fabric


def mark_fabric(fabric, fabric_claims):
    for claim in fabric_claims:
        for row in range(claim.start_row, claim.end_row):
            for col in range(claim.start_col, claim.end_col):
                fabric[row][col] += 1

    return fabric


def count_claim_overlaps(fabric):
    overlap_squares = 0
    for row in fabric:
        for value in row:
            if value >= 2:
                overlap_squares += 1
    return overlap_squares


if __name__ == '__main__':
    main()
