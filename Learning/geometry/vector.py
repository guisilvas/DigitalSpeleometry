from numbers import Real

class Vector:
    def __init__(self, coord, angle, length):
        for value in coord:
            if not isinstance(value, Real):
                raise TypeError("Coordinates must be numeric.")
        self.coord = tuple(coord)
        self.angle = angle
        self.length = self.length()

    def __repr__(self):
        return str("Coordenates: {coord}, Angle to X axis: {angle}, Length: {length}".format(coord = self.coord, angle = self.angle, length = self.length)
    
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
        if self.dimen_diff_of(other):
            raise ValueError("Incompatible dimension.")
        coord = []
        for value in coord:
            coord = x*value
        return Vector(coord)
    
    def dot_prod(self, other):
        if dimen_diff_of(self, other):
            raise ValueError("Incompatible dimension.")
        dot = 0.0
        for i in range(len(self.coord)):
            dot += self.coord[i] * other.coord[i]
        return dot

    def cross_prod(self, other):
        if dimen_diff_of(self, other):
            raise ValueError("Incompatible dimension.")
        coord = []
        
        return Vector(coord)

    def angle_between(self, other):
        if dimen_diff_of(self, other):
            raise ValueError("Incompatible dimension.")
        sum1 = 0.0, length1 = self.length, sum2 = 0.0, length2 = other.length()
        for i in range(len(self.coord)):
            sum1 += self.coord[i] / length1
            sum2 += other.coord[i] / length2
        return cos(sum1 * sum2) ** -1


