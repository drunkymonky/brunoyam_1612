class Shape:
    def __init__(self, color, weight=0):
        self.data = [1, 2, 3]
        self.color = color
        self.weight = weight

    def get(self, i):
        return self.data[i]

    def square(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color='blue'):
        super().__init__(color)
        self.radius = radius
        self.color = 'blue'

    def square(self):
        print('in circle')
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, a, color='blue'):
        super().__init__(color)
        self.a = a

    def square(self):
        return self.a ** 2


circle = Circle(4)
circle.color = 'red'
circle.weight = 10
print(circle.square())

rect = Rectangle(2)
print(rect.square())

data = [circle, rect]


def sum_of_squares(squares):
    """
    :type squares: [opp.oop_example.Shape]
    """
    summa = 0
    for figure in squares:
        summa += figure.square()
    return summa
