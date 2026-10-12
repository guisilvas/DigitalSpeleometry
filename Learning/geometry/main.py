from point import Point

p1 = Point([0,1])
p2 = Point([0,2])
p3 = Point([0,0])

print("Distance from a = {a} to b = {b} is {distance:.3f}".format(a = [p1], b = [p2], distance = p1.euclidean_dist_to(p2)))
p3 = p2.diff(p1)
print("c = b - a = {p3}".format(p3 = p3))
p4 = p2.sum(p1)
print("c = b + a = {p4}".format(p4 = p4))

p5 = Point([3.8, 5.0, 6.3])
print("p5 = {a}".format(a = [p5]))

p6 = p5.filter_coord(4.0)
print("Point without coords lower than 4.0, p6 = {a}".format(a = [p6]))
