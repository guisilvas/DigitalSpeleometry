from point import Point

p1 = Point([0,1])
p2 = Point([0,2])
p3 = Point([0,0])

print("Distance from a = {a} to b = {b} is {distance:.3f}".format(a = [p1], b = [p2], distance = p1.euclidean_dist_to(p2)))
p3 = p1.minus(p2)
print("c = b - a = {p3}".format(p3 = p3))

p4 = Point([3.8, 5.0, 6.3])
print("p3 = {a}".format(a = [p4]))

p5 = p4.significant_coord(4.0)
print("Point without coords lower than 4.0, p5 = {a}".format(a = [p5]))
