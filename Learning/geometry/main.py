from point import Point

p1 = Point([0, 1])
p2 = Point([0, 2])
p3 = Point([0, 0])

# Test distance
distance = p1.euclidean_dist_to(p2)
print(f"Distance from {p1} to {p2} is {distance:.3f}")

# Test midpoint
midpoint = p1.mid_point(p2)
print(f"Midpoint between {p1} and {p2} is {midpoint}")

# Test vector between points
vector = p1.vector_to(p2)
print(f"Vector from {p1} to {p2} is {vector}")

# Test dimension
print(f"Dimension of p1 is {p1.dim}")

# Test equality
print(f"p1 equals p2: {p1.equal_to(p2)}")
print(f"p1 equals p3: {p1.equal_to(p3)}")

