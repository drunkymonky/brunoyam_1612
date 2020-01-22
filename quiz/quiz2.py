class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


import unittest as ut


# Test Driven Development
class PointTest(ut.TestCase):
    def assertNotRaise(self, foo):
        try:
            foo()
        except:
            self.fail('run failed')

    def test_constructor(self):
        self.assertNotRaise(lambda: Point(1, 2))

    def test_add(self):
        p = Point(1, 2)
        p1 = Point(2, 3)
        expected = Point(3, 5)
        actual = p + p1
        self.assertEqual(actual.x, expected.x)
        self.assertEqual(actual.y, expected.y)

    def test_str(self):
        p = Point(1, 3)
        expected = "x=1, y=3"
        actual = str(p)
        self.assertEqual(actual, expected)

    def test_equal(self):
        p = Point(1, 1)
        p1 = Point(1, 1)
        self.assertTrue(p == p1)


ut.main()

# p = Point(1, 2)
# p1 = Point()
# p1.x = 1
# p1.y = 2
#
# p2 = Point(2, 4)
# p3 = p2 + p1
# print(p3)
# # x=3, y= 6
# print(p1 == p2)
# # False
# print(p1 == Point(1, 2))
# True
