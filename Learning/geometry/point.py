from numbers import Real

class Point:
    def __init__(self, coord):
        coord = tuple(coord)
        if len(coord) == 0:
            raise ValueError("Dimension invalid.")
        for value in coord:
            if not isinstance(value, Real):
                raise TypeError("Coordinates must be numeric.")
        self.coord = tuple(coord)

    def __repr__(self):
        return f"{self.coord}"

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

    def minus(self, other):
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] - other.coord[i])
        return Point(coord)

    def plus(self, other):
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] + other.coord[i])
        return Point(coord)

    def euclidean_dist_to(self, other):
        distance = 0.0
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")
        for i in range(len(self.coord)):
            distance += (self.coord[i] - other.coord[i]) ** 2
        return distance ** 0.5
