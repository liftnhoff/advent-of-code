from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x.split(")")

    def part1(self):
        objects_by_name = {}
        for parent_name, child_name in self.input_data:
            parent = objects_by_name.get(parent_name)
            if parent is None:
                parent = SpaceObject(parent_name)
                objects_by_name[parent_name] = parent

            child = objects_by_name.get(child_name)
            if child is None:
                child = SpaceObject(child_name)
                objects_by_name[child_name] = child

            child.set_parent(parent)

        return count_orbits(objects_by_name["COM"])

    def part2(self):
        return None


class SpaceObject:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def set_parent(self, parent: SpaceObject):
        self.parent = parent
        parent.children.append(self)


def count_orbits(space_object: SpaceObject, orbit_count: int = 0) -> int:
    count = 0
    for child in space_object.children:
        count += count_orbits(child, orbit_count + 1)
    return orbit_count + count