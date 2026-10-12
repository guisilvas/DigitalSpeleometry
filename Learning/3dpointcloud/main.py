print("Three Dimensional Points visualized on Python\n")

import math
import numpy as np

# Matrix as an n-dimensional array
X = np.array([
    [8,2,53],
    [11,15,2],
    [9,23,0]
])
print(X)

print()
# ----

# Calc euclidean distance beetwen two points of n cordinates
p1 = [1.04, 2.26, 3.003, 4.22, 5.057]
p2 = [6.045, 7.0, 8.223, 9.92, 9.334]

print("Points:")
print("p1 = ", end=" ")
for i in p1:
    print(i, end=" ")

print()

print("p2 = ", end=" ")
for i in p2:
    print(i, end=" ")

def euclDist(a,b):
    if (len(a) != len(b)):
        return -1
    sum = 0.0
    for i in range (len(a)):
        sum += pow(b[i] - a[i], 2)
    return math.sqrt(sum)

print("\n\nDistance between p1 and p2: {:.3f}".format(euclDist(p1, p2)))

a = [2.55, 5.57, 0.35]
b = [0.33, 4.26, 5.83]
print("\nDistance between a and b: {:.3f}".format(euclDist(a, b)))

print()
# ----
