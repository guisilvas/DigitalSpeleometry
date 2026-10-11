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

    def dimen_diff_of(self, other):
        return len(self.coord) != len(other.coord)

    def significant_coord(self, limit):
        coord = []
        for value in self.coord:
            if value >= limit:
                coord.append(value)
        return Vector(coord)

    def difference(self, other):
        if self.dimen_diff_of(other):
            raise ValueError("Incompatible dimension.")
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] - other.coord[i])
        return Vector(coord)

    def sum(self, other):
        if self.dimen_diff_of(other):
            raise ValueError("Incompatible dimension.")
        coord = []
        for i in range(len(self.coord)):
            coord.append(self.coord[i] + other.coord[i])
        return Vector(coord)

    def scalar_mult(self, x):
        coord = []
        for value in self.coord:
            coord.append(x * value)
        return Vector(coord)
    
    def dot_prod(self, other):
        if self.dimen_diff_of(other):
            raise ValueError("Incompatible dimension.")
        dot = 0.0
        for i in range(len(self.coord)):
            dot += self.coord[i] * other.coord[i]
        return dot

    def angle_between(self, other):
        if dimen_diff_of(self, other):
            raise ValueError("Incompatible dimension.")
        length1 = self.length(), length2 = other.length()
        return acos(self.dot_prod(other) / (length1 * length2))


