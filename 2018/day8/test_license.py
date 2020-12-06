from .license import LicenseTree


class TestLicenseTree:
    def test_part1(self):
        tree = LicenseTree.from_file('day8/data/data.txt')
        value = tree.sum_metadata()
        print(f'\n***** Day 8 Part 1 Answer: {value}')

    def test_part2(self):
        tree = LicenseTree.from_file('day8/data/data.txt')
        value = tree.node_value()
        print(f'\n***** Day 8 Part 2 Answer: {value}')

    def test_sum_metadata(self):
        tree = LicenseTree.from_file('day8/data/test_data.txt')
        assert tree.sum_metadata() == 138

    def test_node_value(self):
        tree = LicenseTree.from_file('day8/data/test_data.txt')
        assert tree.node_value() == 66
