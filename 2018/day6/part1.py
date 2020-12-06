from points import PointCollection


def main():
    points = PointCollection.read_points_file('data/data.txt')

    largest_point = points.point_with_largest_finite_span()
    if largest_point:
        print(largest_point)
        print(largest_point.span_size)
    else:
        print('No largest finite span could be found.')


if __name__ == '__main__':
    main()
