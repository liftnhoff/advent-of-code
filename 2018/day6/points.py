class Point:
    def __init__(self, number, row_index, col_index):
        """
        Args:
            number (int): The identifier for this point.
            row_index (int): The row position corresponding to this Point.
            col_index (int): The column position corresponding to this Point.
        """
        self.number = number
        self.row_index = row_index
        self.col_index = col_index

        self.span_size = 0
        self.span_touches_edge = False

    def __repr__(self):
        return f'Point #{self.number} ({self.row_index},{self.col_index})'

    def manhattan_distance(self, row_index, col_index):
        return abs(self.row_index - row_index) + abs(self.col_index - col_index)


class PointCollection:
    @classmethod
    def read_points_file(cls, data_file):
        """Read a collection of 2D points from a file.

        Args:
            data_file (str): The path to a file containing newline separated 2D point
                definition tuples with the form `col_index, row_index`.

        Returns:
            PointCollection: The collection of points specified in the data_file.
        """
        points = PointCollection()
        with open(data_file) as fid:
            for count, line in enumerate(fid, start=1):
                col_index, row_index = line.strip().split(', ')
                points.add_point(Point(count, int(row_index), int(col_index)))

        return points

    def __init__(self):
        self._points = []
        self.min_row_index = 0
        self.max_row_index = 0
        self.min_col_index = 0
        self.max_col_index = 0

        self.row_edges = []
        self.col_edges = []

    def __repr__(self):
        return f'PointCollection({self._points})'

    def add_point(self, point):
        """
        Args:
            point (Point): The Point to add to this PointCollection.
        """
        if not isinstance(point, Point):
            raise TypeError('Only Point objects can be added to a PointCollection.')
        self._points.append(point)

        if point.row_index < self.min_row_index:
            self.min_row_index = point.row_index
        elif point.row_index > self.max_row_index:
            self.max_row_index = point.row_index

        if point.col_index < self.min_col_index:
            self.min_col_index = point.col_index
        elif point.col_index > self.max_col_index:
            self.max_col_index = point.col_index

    def point_with_largest_finite_span(self):
        """Find the point with the largest "nearest point span".

        Returns:
            (Point or None): The Point with the largest finite span or None if all spans
                are infinite.
        """
        self._calculate_nearest_point_spans()
        largest_span_point = self._get_largest_finite_span_point()
        return largest_span_point

    def _calculate_nearest_point_spans(self):
        self.row_edges = [self.min_row_index, self.max_row_index]
        self.col_edges = [self.min_col_index, self.max_col_index]
        for row_index in range(self.min_row_index, self.max_row_index + 1):
            for col_index in range(self.min_col_index, self.max_col_index + 1):
                self._update_closest_point(row_index, col_index)

    def _update_closest_point(self, row_index, col_index):
        closest_point = self._closest_point(row_index, col_index)
        if closest_point:
            closest_point.span_size += 1
            if row_index in self.row_edges or col_index in self.col_edges:
                closest_point.span_touches_edge = True

    def _closest_point(self, row_index, col_index):
        """Find the closest point in this collection to a given grid location.

        Args:
            row_index (int): Grid row location.
            col_index (int): Grid column location.

        Returns:
            (Point or None): The closest Point or None if several Points are the same
                distance from the input location.
        """
        min_distance = self.max_row_index + self.max_col_index + 2
        min_distance_point = None
        for point in self._points:
            distance = point.manhattan_distance(row_index, col_index)
            if distance < min_distance:
                min_distance = distance
                min_distance_point = point
            elif distance == min_distance:
                min_distance_point = None

        return min_distance_point

    def _get_largest_finite_span_point(self):
        largest_span_point = None
        for point in self._points:
            if point.span_touches_edge:
                continue

            if largest_span_point:
                if largest_span_point.span_size < point.span_size:
                    largest_span_point = point
            else:
                largest_span_point = point

        return largest_span_point

    def area_of_region_near_all_points(self, max_distance):
        """Calculate the area of the region within a given distance of all of the points.

        Args:
            max_distance (int): The distance limit.

        Returns:
            int: The area of the region.
        """
        region_area = 0
        for row_index in range(self.min_row_index, self.max_row_index + 1):
            for col_index in range(self.min_col_index, self.max_col_index + 1):
                if self._is_distance_sum_within_limit(row_index, col_index, max_distance):
                    region_area += 1
        return region_area

    def _is_distance_sum_within_limit(self, row_index, col_index, max_distance):
        distance = 0
        for point in self._points:
            distance += point.manhattan_distance(row_index, col_index)
            if distance >= max_distance:
                break

        if distance < max_distance:
            return True
        else:
            return False
