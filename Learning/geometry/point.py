from numbers import Real

class Point:
    def __init__(self, coord):
        coord = tuple(coord)
        if len(coord) == 0:
            raise ValueError("Dimension invalid.")
        for value in coord:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("Coordinates must be numeric.")
        self.coord = coord

    def __repr__(self):
        return f"{self.coord}"

    def check_compatible(self, other):
        if not isinstance(other, Point):
            raise TypeError("Must be a point.")
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")

    def has_diff_dim(self, other):
        return len(self.coord) != len(other.coord)

    def filter_coord(self, limit):
        coord = []
        for value in self.coord:
            if value >= limit:
                coord.append(value)
            else:
                coord.append(0)
        return Point(coord)

    def diff(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(len(self.coord)):
            coord.append(other.coord[i] - self.coord[i])
        return Point(coord)

    def sum(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] + other.coord[i])
        return Point(coord)

    def euclidean_dist_to(self, other):
        self.check_compatible(other)
        distance = 0.0
        for i in range(len(self.coord)):
            distance += (self.coord[i] - other.coord[i]) ** 2
        return distance ** 0.5

    def mid_point(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(len(self.coord)):
            coord.append((other.coord[i] + self.coord[i]) / 2)
        return Point(coord)

    def vector_to(self, other):
        self.check_compatible(other)
        from vector import Vector
        coord = []
        for i in range(len(self.coord)):
            coord.append(other.coord[i] - self.coord[i])
        return Vector(coord)
