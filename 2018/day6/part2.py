from points import PointCollection


def main():
    points = PointCollection.read_points_file('data/data.txt')

    limit = 10000
    area = points.area_of_region_near_all_points(limit)
    print(area)


if __name__ == '__main__':
    main()
