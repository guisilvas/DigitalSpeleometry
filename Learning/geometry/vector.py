from numbers import Real

class Vector:
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

    # Print vector
    def __repr__(self):
        return f"Vector{self.coord}"

    # Vector length
    def length(self):
        length = 0.0
        for value in self.coord:
            length += value ** 2
        return length ** 0.5
    
    # Verify compatibility with other vector
    def check_compatible(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Must be a vector.")
        if self.has_diff_dim(other):
            raise ValueError("Incompatible dimension.")

    # Verify dim of other vector
    def has_diff_dim(self, other):
        return self.dim != other.dim

    # Vector with only significant coords
    def significant_coord(self, limit):
        coord = []
        for value in self.coord:
            if value >= limit:
                coord.append(value)
            else:
                coord.appen(0)
        return Vector(coord)

    # Difference to other vector
    def diff(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(self.dim):
            coord.append(self.coord[i] - other.coord[i])
        return Vector(coord)

    # Sum with other vector
    def sum(self, other):
        self.check_compatible(other)
        coord = []
        for i in range(self.dim):
            coord.append(self.coord[i] + other.coord[i])
        return Vector(coord)

    # Multiplication to scalar
    def scalar_mult(self, x):
        if isinstance(x, bool) or not isinstance(x, Real):
            raise TypeError("Scalar must be a real number.")
        coord = []
        for value in self.coord:
            coord.append(x * value)
        return Vector(coord)
    
    # Dot prod to other vector
    def dot_prod(self, other):
        self.check_compatible(other)
        dot = 0.0
        for i in range(len(self.coord)):
            dot += self.coord[i] * other.coord[i]
        return dot

    # Angle to other vector
    def angle_between(self, other):
        self.check_compatible(other)
        from math import acos
        length1 = self.length()
        length2 = other.length()
        if length1 == 0 or length2 == 0:
            raise ValueError("Zero vector dont have angle.")
        cosine = self.dot_prod(other) / (length1 * length2)
        cosine = max(-1.0, min(1.0, cosine))
        return acos(cosine)
