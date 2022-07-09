from turtle import width


class Rectangle:
    def __init__(self, length, weidth, color):
        self.length = length
        self.weidth = weidth
        self.color = color


my_rectangle = Rectangle(5, 4, "Blue")


class Circle:
    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(8)

print(my_rectangle.color)

# modify the values
my_rectangle.length = 7
