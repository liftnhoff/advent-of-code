from base.solution import AdventOfCodeSolutionBase


class Solution(AdventOfCodeSolutionBase):
    def data_parser(self):
        return lambda x: x

    def part1(self):
        image = Image(self.input_data[0])

        min_zero_count = 999_999
        min_zero_layer = 0
        for index, layer in enumerate(image.layers):
            zero_count = sum(1 for v in layer if v == 0)
            if zero_count < min_zero_count:
                min_zero_count = zero_count
                min_zero_layer = index

        return (
            sum(1 for v in image.layers[min_zero_layer] if v == 1)
            * sum(1 for v in image.layers[min_zero_layer] if v == 2)
        )

    def part2(self):
        image = Image(self.input_data[0])

        visual = image.layers[0][:]
        for value_index in range(len(image.layers[0])):
            for layer_index in range(1, len(image.layers)):
                if visual[value_index] == 2:
                    visual[value_index] = image.layers[layer_index][value_index]

        row = []
        for index, value in enumerate(visual):
            if index % 25 == 0:
                print("".join(v for v in row))
                row = []
            if value == 1:
                row.append("#")
            else:
                row.append(" ")
        print("".join(v for v in row))

        return None


class Image:
    WIDTH = 25
    HEIGHT = 6

    def __init__(self, values: str):
        self.layers = [[]]
        for value in values:
            if len(self.layers[-1]) == self.WIDTH * self.HEIGHT:
                self.layers.append([])
            self.layers[-1].append(int(value))

