from part1 import make_fabric, read_fabric_claims


def main():
    fabric_claims = read_fabric_claims('data.txt')
    fabric = make_fabric(fabric_claims)

    claim_ids = find_non_overlapping_claims(fabric, fabric_claims)
    print(claim_ids)


def find_non_overlapping_claims(fabric, fabric_claims):
    claim_ids = {claim.claim_id for claim in fabric_claims}
    overlapping_claim_ids = set()
    for claim in fabric_claims:
        for row in range(claim.start_row, claim.end_row):
            for col in range(claim.start_col, claim.end_col):
                existing_claim_id = fabric[row][col]
                if existing_claim_id == 0:
                    fabric[row][col] = claim.claim_id
                else:
                    overlapping_claim_ids.add(existing_claim_id)
                    overlapping_claim_ids.add(claim.claim_id)

    claim_ids -= overlapping_claim_ids
    return claim_ids


if __name__ == '__main__':
    main()
