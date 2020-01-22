class Point:
    pass


p = Point(1, 2)
p1 = Point()
p1.x = 1
p1.y = 2

p2 = Point(2, 4)
p3 = p2 + p1
print(p3)
# x=3, y= 6
print(p1 == p2)
# False
print(p1 == Point(1, 2))
# True