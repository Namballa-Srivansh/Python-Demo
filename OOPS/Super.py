# Super() = function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
     def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("Yellow", True, 7, 8)

circle.describe()

# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)

# print(square.color)
# print(square.is_filled)
# print(square.width)

# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)