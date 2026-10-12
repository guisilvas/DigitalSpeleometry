from numbers import Real

class Point:
    # Class constructor
    def __init__(self, coord):
        coord = tuple(coord)
        if len(coord) == 0:
            raise ValueError("Dimension invalid.")
        for value in coord:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("Coordinates must be numeric.")
        self.coord = coord

    # Dimension property
    @property
    def dim(self):
        return len(self.coord)

    # Print object
    def __repr__(self):
        return f"Point{self.coord}"
    
    # Verify if other point have different dim
    def has_diff_dim(self, other):
        return self.dim != other.dim

    # Verify compatibility with other point by dim
    def check_compatible(self, other):
        if not isinstance(other, Point):
            raise TypeError("Must be a point.")
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")

    # Calc euclidean dist to other point
    def euclidean_dist_to(self, other):
        self.check_compatible(other)
        distance = 0.0
        for i in range(self.dim):
            distance += (self.coord[i] - other.coord[i]) ** 2
        return distance ** 0.5

    # Calc midpoint between other point
    def mid_point(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(self.dim):
            coord.append((other.coord[i] + self.coord[i]) / 2)
        return Point(coord)

    # Creates a vector to other point
    def vector_to(self, other):
        self.check_compatible(other)
        from vector import Vector
        coord = []
        for i in range(self.dim):
            coord.append(other.coord[i] - self.coord[i])
        return Vector(coord)

    # Check whether is equal to other point
    def equal_to(self, other):
        self.check_compatible(other)
        return self.coord == other.coord

    # Translate by vector
    def translate(self, vector):
        from vector import Vector
        if not isinstance(vector, Vector):
            raise TypeError("Must be a vector.")
        if self.dim != len(vector.coord):
            raise ValueError("Incompatible dimension.")
        coord = []
        for i in range(self.dim):
            coord.append(self.coord[i] + vector.coord[i])
        return Point(coord)

    # Squared dist to other point
    def squared_dist_to(self, other):
        self.check_compatible(other)
        distance_squared = 0.0
        for i in range(self.dim):
            distance_squared += (self.coord[i] - other.coord[i]) ** 2
        return distance_squared
