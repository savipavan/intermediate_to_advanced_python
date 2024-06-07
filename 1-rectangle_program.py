"""
Development steps:
- Write down the objects on paper
- Writing a class for each object
- Writing methods for each class
- Calling the classes and their methods
"""
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False

    # def distance_from_point(self, x, y):
    #     return ((self.x -x)** 2 + \
    #             (self.y - y)** 2) ** 0.5


class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def area(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)

# Create rectangle object
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.lowleft.x, ",",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, ",",
      rectangle.upright.y)

# Get point and area from user
user_point = Point(float(input("Guess X: ")),
                   float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game results
print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))

print("Your area was off by: ", rectangle.area() - user_area)
