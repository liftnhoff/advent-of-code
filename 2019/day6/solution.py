from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x.split(")")

    def part1(self):
        objects_by_name = build_object_orbits(self.input_data)
        return count_orbits(objects_by_name["COM"])

    def part2(self):
        objects_by_name = build_object_orbits(self.input_data)
        you_orbits = list(reversed(trace_orbit_dependencies(objects_by_name["YOU"])))
        san_orbits = list(reversed(trace_orbit_dependencies(objects_by_name["SAN"])))
        diverge_index = 0
        for index in range(len(you_orbits)):
            if you_orbits[index] != san_orbits[index]:
                diverge_index = index - 1
                break

        offset_for_starts_and_common_object = 4
        return (
            len(you_orbits[diverge_index:])
            + len(san_orbits[diverge_index:])
            - offset_for_starts_and_common_object
        )


class SpaceObject:
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def set_parent(self, parent: SpaceObject):
        self.parent = parent
        parent.children.append(self)


def build_object_orbits(orbit_pairs: list[list[str]]) -> dict[str, SpaceObject]:
    objects_by_name = {}
    for parent_name, child_name in orbit_pairs:
        parent = objects_by_name.get(parent_name)
        if parent is None:
            parent = SpaceObject(parent_name)
            objects_by_name[parent_name] = parent

        child = objects_by_name.get(child_name)
        if child is None:
            child = SpaceObject(child_name)
            objects_by_name[child_name] = child

        child.set_parent(parent)

    return objects_by_name


def count_orbits(space_object: SpaceObject, orbit_count: int = 0) -> int:
    count = 0
    for child in space_object.children:
        count += count_orbits(child, orbit_count + 1)
    return orbit_count + count


def trace_orbit_dependencies(space_object: SpaceObject) -> list[str]:
    orbit_dependencies = [space_object.name]
    while space_object.parent is not None:
        space_object = space_object.parent
        orbit_dependencies.append(space_object.name)

    return orbit_dependencies
