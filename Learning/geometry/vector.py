from numbers import Real

class Vector:
    def __init__(self, coord):
        coord = tuple(coord)
        if len(coord) == 0:
            raise ValueError("Dimension invalid.")
        for value in coord:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("Coordinates must be numeric.")
        self.coord = coord

    def __repr__(self):
        return str(self.coord)
    
    def length(self):
        length = 0.0
        for value in self.coord:
            length += value ** 2
        return length ** 0.5
    
    def check_compatible(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Must be a vector.")
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")

    def has_diff_dim(self, other):
        return len(self.coord) != len(other.coord)

    def significant_coord(self, limit):
        coord = []
        for value in self.coord:
            if value >= limit:
                coord.append(value)
        return Vector(coord)

    def difference(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] - other.coord[i])
        return Vector(coord)

    def sum(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] + other.coord[i])
        return Vector(coord)

    def scalar_mult(self, x):
        if not isinstace(x, Read):
            raise TypeError("Scalar must be a real number.")
        coord = []
        for value in self.coord:
            coord.append(x * value)
        return Vector(coord)
    
    def dot_prod(self, other):
        self.check_compatible(other):
        dot = 0.0
        for i in range(len(self.coord)):
            dot += self.coord[i] * other.coord[i]
        return dot

    def angle_between(self, other):
        self.check_compatible(other)
        length1 = self.length()
        length2 = other.length()
        from math import acos
        return acos(self.dot_prod(other) / (length1 * length2))
