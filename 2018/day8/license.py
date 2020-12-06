class LicenseTree:
    def __init__(self, start_node):
        self.start_node = start_node

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'LicenseTree({self.start_node})'

    @classmethod
    def from_file(cls, filename):
        with open(filename) as fid:
            data = fid.read().strip().split(' ')
            data = [int(value) for value in reversed(data)]
            start_node = cls._read_node(data)

        return LicenseTree(start_node)

    @classmethod
    def _read_node(cls, data):
        child_count = data.pop()
        metadata_count = data.pop()

        node = Node()
        for _ in range(child_count):
            node.add_child(cls._read_node(data))

        for _ in range(metadata_count):
            node.add_metadata(data.pop())

        return node

    def sum_metadata(self, node=None):
        if node is None:
            node = self.start_node

        current_sum = 0
        for child in node.children:
            current_sum += self.sum_metadata(node=child)
        current_sum += sum(node.metadata)

        return current_sum

    def node_value(self, node=None):
        if node is None:
            node = self.start_node

        current_value = 0
        child_count = len(node.children)
        if child_count == 0:
            current_value += sum(node.metadata)
        else:
            for index in node.metadata:
                if index <= 0 or index > child_count:
                    continue
                current_value += self.node_value(node=node.children[index - 1])

        return current_value


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'Node({self.children}, {self.metadata})'

    def add_child(self, node):
        self.children.append(node)

    def add_metadata(self, value):
        self.metadata.append(value)
